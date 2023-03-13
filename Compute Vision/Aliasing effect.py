import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

# Load a high-resolution image
img = misc.ascent()
print('img shape:',img.shape)

# Define the subsampling factor
factor = 4

# Subsample the image
subsampled_img = img[::factor, ::factor]

# Plot the original and subsampled images
fig, sub = plt.subplots(1, 2, figsize=(10, 5))
sub[0].imshow(img, cmap='gray')
sub[0].set_title('Original Image')
sub[1].imshow(subsampled_img, cmap='gray')
sub[1].set_title('Subsampled Image (Factor {})'.format(factor))
plt.show()
