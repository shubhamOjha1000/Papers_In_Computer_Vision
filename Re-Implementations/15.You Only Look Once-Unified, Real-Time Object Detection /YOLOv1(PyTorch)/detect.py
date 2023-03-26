import torch
import torchvision.transforms as transforms

import os
import cv2
import argparse
import numpy as np

from nets.nn import YOLOv1
from utils.utils import nms

# VOC class names and BGR color.
VOC_CLASS_BGR = {
    'aeroplane': (128, 0, 0),
    'bicycle': (0, 128, 0),
    'bird': (128, 128, 0),
    'boat': (0, 0, 128),
    'bottle': (128, 0, 128),
    'bus': (0, 128, 128),
    'car': (128, 128, 128),
    'cat': (64, 0, 0),
    'chair': (192, 0, 0),
    'cow': (64, 128, 0),
    'diningtable': (192, 128, 0),
    'dog': (64, 0, 128),
    'horse': (192, 0, 128),
    'motorbike': (64, 128, 128),
    'person': (192, 128, 128),
    'pottedplant': (0, 64, 0),
    'sheep': (128, 64, 0),
    'sofa': (0, 192, 0),
    'train': (128, 192, 0),
    'tvmonitor': (0, 64, 128)
}


def visualize_boxes(image_bgr, boxes, class_names, probs, name_bgr_dict=None, line_thickness=2):
    if name_bgr_dict is None:
        name_bgr_dict = VOC_CLASS_BGR

    image_boxes = image_bgr.copy()
    for box, class_name, prob in zip(boxes, class_names, probs):
        # Draw box on the image.
        left_top, right_bottom = box
        left, top = int(left_top[0]), int(left_top[1])
        right, bottom = int(right_bottom[0]), int(right_bottom[1])
        bgr = name_bgr_dict[class_name]
        cv2.rectangle(image_boxes, (left, top), (right, bottom), bgr, thickness=line_thickness)

        # Draw text on the image.
        text = '%s %.2f' % (class_name, prob)
        size, baseline = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.5, thickness=2)
        text_w, text_h = size

        x, y = left, top
        x1y1 = (x, y)
        x2y2 = (x + text_w + line_thickness, y + text_h + line_thickness + baseline)
        cv2.rectangle(image_boxes, x1y1, x2y2, bgr, -1)
        cv2.putText(image_boxes, text, (x + line_thickness, y + 2 * baseline + line_thickness),
                    cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.4, color=(255, 255, 255), thickness=1, lineType=8)

    return image_boxes


class YOLODetector:
    def __init__(self,
                 model_path, class_name_list=None, mean_rgb=[122.67891434, 116.66876762, 104.00698793],
                 conf_thresh=0.1, prob_thresh=0.1, nms_thresh=0.5):

        use_gpu = torch.cuda.is_available()
        assert use_gpu, 'Current implementation does not support CPU mode. Enable CUDA.'

        # Load YOLO model.
        print("Loading YOLO model...")
        yolo = YOLOv1()

        self.yolo = torch.nn.DataParallel(yolo)
        self.yolo.load_state_dict(torch.load(model_path)['state_dict'])
        self.yolo.cuda()
        if torch.cuda.device_count() > 1:
            self.yolo = torch.nn.DataParallel(self.yolo)
        print("Done loading!")

        self.yolo.eval()

        self.S = self.yolo.module.module.FS
        self.B = self.yolo.module.module.NB
        self.C = self.yolo.module.module.NC

        self.class_name_list = class_name_list if (class_name_list is not None) else list(VOC_CLASS_BGR.keys())
        assert len(self.class_name_list) == self.C

        self.mean = np.array(mean_rgb, dtype=np.float32)
        assert self.mean.shape == (3,)

        self.conf_thresh = conf_thresh
        self.prob_thresh = prob_thresh
        self.nms_thresh = nms_thresh

        self.to_tensor = transforms.ToTensor()

        # Warm up.
        dummy_input = torch.zeros((1, 3, 448, 448))
        dummy_input = dummy_input.cuda()
        for i in range(10):
            self.yolo(dummy_input)

    def detect(self, image_bgr, image_size=448):
        h, w, _ = image_bgr.shape
        img = cv2.resize(image_bgr, dsize=(image_size, image_size), interpolation=cv2.INTER_LINEAR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # assuming the model is trained with RGB images.
        img = (img - self.mean) / 255.0
        img = self.to_tensor(img)  # [image_size, image_size, 3] -> [3, image_size, image_size]
        img = img[None, :, :, :]  # [3, image_size, image_size] -> [1, 3, image_size, image_size]
        img = img.cuda()

        with torch.no_grad():
            pred_tensor = self.yolo(img)
        pred_tensor = pred_tensor.cpu().data
        pred_tensor = pred_tensor.squeeze(0)  # squeeze batch dimension.

        # Get detected boxes_detected, labels, confidences, class-scores.
        boxes_normalized_all, class_labels_all, confidences_all, class_scores_all = self.decode(pred_tensor)
        if boxes_normalized_all.size(0) == 0:
            return [], [], []  # if no box found, return empty lists.

        # Apply non maximum supression for boxes of each class.
        boxes_normalized, class_labels, probs = [], [], []

        for class_label in range(len(self.class_name_list)):
            mask = (class_labels_all == class_label)
            if torch.sum(mask) == 0:
                continue  # if no box found, skip that class.

            boxes_normalized_masked = boxes_normalized_all[mask]
            class_labels_maked = class_labels_all[mask]
            confidences_masked = confidences_all[mask]
            class_scores_masked = class_scores_all[mask]

            ids = nms(boxes_normalized_masked, confidences_masked, nms_thresh=self.nms_thresh)

            boxes_normalized.append(boxes_normalized_masked[ids])
            class_labels.append(class_labels_maked[ids])
            probs.append(confidences_masked[ids] * class_scores_masked[ids])

        boxes_normalized = torch.cat(boxes_normalized, 0)
        class_labels = torch.cat(class_labels, 0)
        probs = torch.cat(probs, 0)

        # Postprocess for box, labels, probs.
        boxes_detected, class_names_detected, probs_detected = [], [], []
        for b in range(boxes_normalized.size(0)):
            box_normalized = boxes_normalized[b]
            class_label = class_labels[b]
            prob = probs[b]

            x1, x2 = w * box_normalized[0], w * box_normalized[2]  # unnormalize x with image width.
            y1, y2 = h * box_normalized[1], h * box_normalized[3]  # unnormalize y with image height.
            boxes_detected.append(((x1, y1), (x2, y2)))

            class_label = int(class_label)  # convert from LongTensor to int.
            class_name = self.class_name_list[class_label]
            class_names_detected.append(class_name)

            prob = float(prob)  # convert from Tensor to float.
            probs_detected.append(prob)

        return boxes_detected, class_names_detected, probs_detected

    def decode(self, pred_tensor):

        S, B, C = self.S, self.B, self.C
        boxes, labels, confidences, class_scores = [], [], [], []

        cell_size = 1.0 / float(S)

        conf = pred_tensor[:, :, 4].unsqueeze(2)  # [S, S, 1]
        for b in range(1, B):
            conf = torch.cat((conf, pred_tensor[:, :, 5 * b + 4].unsqueeze(2)), 2)
        conf_mask = conf > self.conf_thresh  # [S, S, B]

        # TBM, further optimization may be possible by replacing the following for-loops with tensor operations.
        for i in range(S):  # for x-dimension.
            for j in range(S):  # for y-dimension.
                class_score, class_label = torch.max(pred_tensor[j, i, 5 * B:], 0)

                for b in range(B):
                    conf = pred_tensor[j, i, 5 * b + 4]
                    prob = conf * class_score
                    if float(prob) < self.prob_thresh:
                        continue

                    # Compute box corner (x1, y1, x2, y2) from tensor.
                    box = pred_tensor[j, i, 5 * b: 5 * b + 4]
                    x0y0_normalized = torch.FloatTensor([i,
                                                         j]) * cell_size  # cell left-top corner. Normalized from 0.0 to 1.0 w.r.t. image width/height.
                    xy_normalized = box[
                                    :2] * cell_size + x0y0_normalized  # box center. Normalized from 0.0 to 1.0 w.r.t. image width/height.
                    wh_normalized = box[
                                    2:]  # Box width and height. Normalized from 0.0 to 1.0 w.r.t. image width/height.
                    box_xyxy = torch.FloatTensor(4)  # [4,]
                    box_xyxy[:2] = xy_normalized - 0.5 * wh_normalized  # left-top corner (x1, y1).
                    box_xyxy[2:] = xy_normalized + 0.5 * wh_normalized  # right-bottom corner (x2, y2).

                    # Append result to the lists.
                    boxes.append(box_xyxy)
                    labels.append(class_label)
                    confidences.append(conf)
                    class_scores.append(class_score)

        if len(boxes) > 0:
            boxes = torch.stack(boxes, 0)  # [n_boxes, 4]
            labels = torch.stack(labels, 0)  # [n_boxes, ]
            confidences = torch.stack(confidences, 0)  # [n_boxes, ]
            class_scores = torch.stack(class_scores, 0)  # [n_boxes, ]
        else:
            # If no box found, return empty tensors.
            boxes = torch.FloatTensor(0, 4)
            labels = torch.LongTensor(0)
            confidences = torch.FloatTensor(0)
            class_scores = torch.FloatTensor(0)

        return boxes, labels, confidences, class_scores


if __name__ == '__main__':
    # Paths to input/output images.
    parser = argparse.ArgumentParser(description='YOLOv1 implementation using PyTorch')
    parser.add_argument('--weight', default='weights/final.pth', help='Model path')
    parser.add_argument('--in_path', default='../../Datasets/VOC/test/IMAGES/000004.jpg', help='Input image path')
    parser.add_argument('--out_path', default='result.jpg', help='Output image path')

    args = parser.parse_args()
    # GPU device on which yolo is loaded.
    gpu_id = 0

    # Load model.
    yolo = YOLODetector(args.weight, conf_thresh=0.6, prob_thresh=0.6, nms_thresh=0.35)

    # Load image.
    image = cv2.imread(args.in_path)

    # Detect objects.
    boxes, class_names, probs = yolo.detect(image)

    # Visualize.
    image_boxes = visualize_boxes(image, boxes, class_names, probs)

    # Output detection result as an image.
    cv2.imwrite(args.out_path, image_boxes)
