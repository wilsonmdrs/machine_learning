# Image I/O
import imageio
# Image processing
from skimage import color, img_as_float
# Plots
import matplotlib.pyplot as pp
# Image processing
from skimage import exposure
# Arrangement processing

import numpy as np

np.get_include()

# Read image
monty = imageio.imread('../images/img.png')

# Convert the image to float and gray
monty_gray = color.rgb2gray(img_as_float(monty))

# Print shape and data type of images
print(f'\nMonty shape {monty.shape} and type {monty.dtype}\n')
print(f'Monty gray shape {monty_gray.shape} and type {monty_gray.dtype}', end='\n' * 2)

# Plot image monty gray
pp.figure(figsize=(10, 5))
pp.imshow(monty_gray, cmap='gray')
pp.axis('off')
pp.title('Monty Python')
pp.show()

# Histogram equalization
monty_hist = exposure.equalize_hist(monty_gray)


# Plot normal and equalized image
fig, ax = pp.subplots(2, 2, figsize=(10, 5))  # Lines and cols
cache = [(monty_gray, 'Monty Python'), (monty_hist, 'Monty Python Equalized')]
for indice, image in zip(range(0, 2), cache):

    ax[indice, 0].imshow(image[0], cmap='gray')

    ax[indice, 0].set_title(image[1])

    ax[indice, 0].axis('off')

    weights = np.ones(image[0].ravel().shape) / float(image[0].size)

    ax[indice, 1].hist(image[0].flatten(), bins=256, weights=weights)

pp.show()