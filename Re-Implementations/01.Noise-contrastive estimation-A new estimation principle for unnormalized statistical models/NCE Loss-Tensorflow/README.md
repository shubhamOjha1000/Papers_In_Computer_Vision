# Keras NCE-loss

- **Keras implemenation of the candidate sampling technique called Noise Contrastive Estimation (NCE)**. 
- This is a **Keras Layer which uses the tensorflow implementation of NCE loss**.

- <ins>Paper</ins> : [**Gutmann, Hyvarinen. Noise-contrastive estimation: A new estimation principle for unnormalized statistical models. AISTATS 2010**](https://proceedings.mlr.press/v9/gutmann10a/gutmann10a.pdf)







```python
from keras.layers import (
    Input,
    Dense,
    Embedding,
    Flatten,
)
from keras.models import Model
import keras.backend as K
import numpy as np
from nce import NCE


def build(NUM_ITEMS, num_users, k):

    iid = Input(shape=(1,), dtype="int32", name="iids")
    targets = Input(shape=(1,), dtype="int32", name="target_ids")

    item_embedding = Embedding(
        input_dim=NUM_ITEMS, output_dim=k, input_length=1, name="item_embedding"
    )
    selected_items = Flatten()(item_embedding(iid))

    h1 = Dense(k // 2, activation="relu", name="hidden")(selected_items)

    sm_logits = NCE(num_users, name="nce")([h1, targets])

    model = Model(inputs=[iid, targets], outputs=[sm_logits])
    return model


K = 10
SAMPLE_SIZE = 10000
num_items = 10000
NUM_USERS = 1000000 #THIS IS SIZE OF SOFTMAX

model = build(num_items, NUM_USERS, K)
model.compile(optimizer="adam", loss=None)
model.summary()

x = np.random.random_integers(num_items - 1, size=SAMPLE_SIZE)
y = np.ones(SAMPLE_SIZE)
X = [x, y]
print(x.shape, y.shape)

model.fit(x=X, batch_size=100, epochs=1)

```

