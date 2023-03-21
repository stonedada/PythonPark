import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage.segmentation import watershed
from skimage.feature import peak_local_max
from skimage import data


image = data.coins()
image = ndi.gaussian_filter(image, 1)

# Create a marker image of the coins
markers = np.zeros_like(image)
markers[image < 30] = 1
markers[image > 150] = 2

print(markers)
# Perform watershed segmentation
segmentation = watershed(image, markers)

# Plot the original image and the segmentation result
fig, axes = plt.subplots(ncols=2, figsize=(8, 3))
ax0, ax1 = axes

ax0.imshow(image, cmap='gray')
ax0.set_title('Original Image')

ax1.imshow(segmentation, cmap='gray')
ax1.set_title('Segmentation')

for ax in axes:
    ax.axis('off')

plt.tight_layout()
plt.show()
