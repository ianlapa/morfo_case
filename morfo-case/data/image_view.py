import numpy as np
import matplotlib.pyplot as plt

# this is just a test

# path to image
img = np.load("data/batch_1/img_0.npy")

# Viz
plt.imshow(img)
plt.title("Image 0 - img_0.npy")
plt.axis("off")
plt.show()
