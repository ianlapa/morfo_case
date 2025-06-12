import numpy as np
import matplotlib.pyplot as plt

# Caminho para a imagem .npy
img = np.load("data/batch_1/img_0.npy")

# Visualizar
plt.imshow(img)
plt.title("img_0.npy")
plt.axis("off")
plt.show()
