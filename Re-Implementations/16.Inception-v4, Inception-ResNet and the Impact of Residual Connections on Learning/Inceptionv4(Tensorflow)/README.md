# Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning

- This is the **Keras** implementation of [**Inception-v4, Inception-ResNet and the Impact of Residual Connections on Learning**](http://arxiv.org/pdf/1602.07261v1.pdf)


### Arguments
- ### # of GPUs
```sh
- "-g", "--gpus", default='single', type=int 
```
- ###  Train dataset directory
```sh
"-train", "--train_dir", type=str, default="train/"
```
- ###  Validation dataset directory
```sh
"-val", "--val", type=str, default="val/"
```
- ### Checkpoint directory. Default is 'no', in case you're training from scratch
```sh
"-c", "--checkpoint", type=str, default="no"
```
- ### # of Classes
```sh
"-classes", "--num_classes", type=int, required=True
```
- ### # of Epochs 
```sh
"-epochs", "--epochs", type=int, default=1000
```
- ### # Steps per epoch
```sh
"-steps", "--steps_per_epoch", type=int, default=500
```
- ### Learning Rate
```sh
"-lr", "--learning_rate", type=str, default='1e-3'
```



# Example

```sh
python3 inceptionv4.py -g 8 -train train -val val -classes 20 -epochs 100 -steps 500
```

## A little UX

In case you're willing to execute the code on Cloud, and want it to run as a background process,
use Nohup for it. Nohup basically runs the code in background, and you can reach it easily, in case you're willing to see the progress.

- Example to run

```sh
nohup python3 inceptionv4.py -g 8 -train train -val val -classes 20 -epochs 100 -steps 500 &
```
The Nohup will create ```nohup.out``` file.

- To tail the progress via ```nohup.out``` file

```sh
tail -f nohup.out
```

- To cat the whole progress via ```nohup.out``` file

```sh
cat nohup.out
```

## Tensorboard

Tensorboard will create timestamp directory in ```logs``` folder, with the logfile inside.

Run ```tensorboard --logdir logs/'timestamp'/'logfile' to see execute the tensorboard.

- Little trick

In case you're using Google Colab, Cloud or anything that is not running in your local computer, and 
you want a shortcut to update the tensorboard in every period, here's a little script for it:

```sh
import subprocess
from time import sleep

while True:
  subprocess.run('scp username@ip_address:~/'path to the logfile' 'path to local folder', shell=True)
  sleep(5)

```
The integer in sleep() function is number of seconds. Change it according to your preferences.
Run this script in the background, with tensorboard executed, and it'll download the logfile and update it every once in a while.
Tensorboard will update graphs by itself.


### Must-to-know

After nohup is executed, the way to kill the process is via Htop.
Make sure to run it as an administrator.

- Example

```sh
 sudo htop
```


- List the processes via "S", or - which processes are parent ones. The parent processes will have "R" letter as shown in image, and kill them via ```F9```, and then ```9 + Enter```.

![Inception](https://i.ibb.co/mT3cJLR/htop.png?style=centerme)


### Dropout

Use ```0.2``` dropout, as mentioned in official paper. But, in case you're testing it on small dataset, and model overfits, 
you can increase dropout up to 0.8.
We've tested 0.8 dropout on 600 images, and it gave satisfying results for this size of dataset.


# Keras Multi-GPU Bug Workaround

Keras multi-gpu training throws error while trying to load the multi-gpu trained model. We've researched many workarounds, and we found the simpliest one by ourselves.

After you finish initial training on multi-gpu support, and want to use your model to fine-tune it again, you need to do the next:

- Load the multi-gpu-generated model on single gpu, with couple of steps, let's say 50
- Let the single gpu make 50 steps and save (update) the model.
- You're all set - You can fine-tune the single-gpu generated model on Multi-GPU support now.


# Output

```sh

-----------------------------
$ # of GPUs - 8
$ # of Classes - 20
$ Learning Rate - 1e-3
$ Epochs - 1000
-----------------------------

  1/500 [..............................] - ETA: 4:01 - loss: 2.7470 - acc: 0.3125
  2/500 [..............................] - ETA: 4:04 - loss: 2.4298 - acc: 0.4062
  3/500 [..............................] - ETA: 4:03 - loss: 2.3062 - acc: 0.4167
  4/500 [..............................] - ETA: 4:03 - loss: 2.1503 - acc: 0.4453
  5/500 [..............................] - ETA: 4:04 - loss: 1.9956 - acc: 0.4875
  6/500 [..............................] - ETA: 4:05 - loss: 1.9978 - acc: 0.4948
  7/500 [..............................] - ETA: 4:06 - loss: 2.0658 - acc: 0.4777
  8/500 [..............................] - ETA: 4:16 - loss: 2.0575 - acc: 0.4844
  9/500 [..............................] - ETA: 4:23 - loss: 2.1001 - acc: 0.4792
 10/500 [..............................] - ETA: 4:30 - loss: 2.1054 - acc: 0.4781
 11/500 [..............................] - ETA: 4:36 - loss: 2.1133 - acc: 0.4773
 12/500 [..............................] - ETA: 4:40 - loss: 2.1363 - acc: 0.4740
 13/500 [..............................] - ETA: 4:45 - loss: 2.1333 - acc: 0.4760
 14/500 [..............................] - ETA: 4:48 - loss: 2.1472 - acc: 0.4732
 15/500 [..............................] - ETA: 4:50 - loss: 2.1248 - acc: 0.4813
 16/500 [..............................] - ETA: 4:52 - loss: 2.1280 - acc: 0.4805
 17/500 [>.............................] - ETA: 4:54 - loss: 2.1657 - acc: 0.4706
 18/500 [>.............................] - ETA: 4:55 - loss: 2.1685 - acc: 0.4705
 19/500 [>.............................] - ETA: 4:56 - loss: 2.1693 - acc: 0.4688
 20/500 [>.............................] - ETA: 4:57 - loss: 2.1582 - acc: 0.4734
```

### After finishing training, the model will save the best checkpoint in ```checkpoints``` directory.

