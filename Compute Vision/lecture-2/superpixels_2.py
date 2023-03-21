import numpy as np
import matplotlib.pyplot as plt
from skimage.segmentation import slic
from skimage.color import rgb2lab
from scipy.sparse.linalg import eigsh
from PIL import Image

def segment_image(image):
    # Convert image to LAB color space
    image_lab = rgb2lab(image)
    # Generate superpixels using SLIC algorithm
    labels = slic(image_lab, n_segments=100, compactness=10)
    # Construct modified affinity matrix using color information
    affinity = construct_affinity_matrix(image_lab, labels)
    # Normalize affinity matrix
    norm_affinity = affinity / affinity.sum(axis=1, keepdims=True)
    # Compute eigenvectors and eigenvalues of affinity matrix
    vals, vecs = eigsh(norm_affinity, k=2, which='LM', tol=1e-6)
    # Cluster superpixels into segments
    segments = np.argmin(vecs, axis=1)
    # Generate output image
    output = np.zeros_like(image)
    for i in range(len(np.unique(labels))):
        output[labels == i] = plt.cm.tab20(segments[i])[:-1]
    # Convert output image to RGB
    output = (output * 255).astype(np.uint8)
    # Display input and output images
    Image.fromarray(np.hstack((image, output))).show()

def construct_affinity_matrix(image, labels):
    num_labels = len(np.unique(labels))
    height, width, channels = image.shape
    affinity = np.zeros((num_labels, num_labels))
    for i in range(height):
        for j in range(width):
            label1 = labels[i, j]
            if i > 0:
                label2 = labels[i - 1, j]
                dist = np.linalg.norm(image[i, j] - image[i - 1, j])
                affinity[label1, label2] += dist
                affinity[label2, label1] += dist
            if j > 0:
                label2 = labels[i, j - 1]
                dist = np.linalg.norm(image[i, j] - image[i, j - 1])
                affinity[label1, label2] += dist
                affinity[label2, label1] += dist
            if i < height - 1:
                label2 = labels[i + 1, j]
                dist = np.linalg.norm(image[i, j] - image[i + 1, j])
                affinity[label1, label2] += dist
                affinity[label2, label1] += dist
            if j < width - 1:
                label2 = labels[i, j + 1]
                dist = np.linalg.norm(image[i, j] - image[i, j + 1])
                affinity[label1, label2] += dist
                affinity[label2, label1] += dist
    return affinity

# Load images
image1 = np.array(Image.open('fruit-01.jpg'))
image2 = np.array(Image.open('fruit-02.jpg'))
image3 = np.array(Image.open('fruit-03.jpg'))

# Segment images
segment_image(image1)
segment_image(image2)
segment_image(image3)
