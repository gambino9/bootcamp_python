import numpy as np
import matplotlib
from matplotlib import pyplot as plt

from ColorFilter import ColorFilter

cf = ColorFilter()

path_image = "../elon_canaGAN.png"

for f in [cf.to_red, cf.to_green, cf.to_blue, cf.invert]:
    array = plt.imread(path_image)
    plt.imshow(f(array))
    plt.show()

im = cf.to_grayscale(array, "m")
plt.imshow(im, cmap="gray")
plt.show()

im = cf.to_grayscale(array, "w", weight=[0.2126, 0.7152, 0.0722])
plt.imshow(im, cmap="gray")
plt.show()
