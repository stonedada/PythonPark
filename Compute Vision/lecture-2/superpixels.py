import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.color import rgb2lab
from skimage.future import graph
from skimage import io

# Load images
image_names = ['fruit-01.jpg', 'fruit-02.jpg', 'fruit-03.jpg']
images = [io.imread(name) for name in image_names]

# Set up parameters for superpixel segmentation
n_segments = 200
compactness = 10

# Perform superpixel segmentation on each image
segments = [slic(image, n_segments=n_segments, compactness=compactness) for image in images]

# Convert images to LAB color space for computing color distances
lab_images = [rgb2lab(image) for image in images]

# Compute mean color of each superpixel
mean_colors = [graph.cut_normalized(lab_image, segments[i], mode='mean') for i, lab_image in enumerate(lab_images)]

# Compute affinity matrix using modified formula
sigma = 50
affinities = [graph.rag_mean_color(image, segments[i], mean_colors[i], mode='similarity', sigma=sigma) for i, image in enumerate(images)]

# Perform normalized cuts on affinity matrix to obtain segmentation
segs = [graph.cut_normalized(segments[i], affinities[i]) for i in range(len(images))]

# Display results
for i, image in enumerate(images):
    plt.figure(figsize=(8,8))
    plt.imshow(graph.mark_boundaries(image, segs[i]))
    plt.axis('off')
    plt.show()
