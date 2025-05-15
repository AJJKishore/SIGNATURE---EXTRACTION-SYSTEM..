
import cv2
import numpy as np
from skimage import measure, morphology
from skimage.measure import regionprops
import os

def extract_signatures(input_path, output_dir='./outputs'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    img = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise ValueError(f"Could not read image from {input_path}")

    _, img_bin = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    blobs_labels = measure.label(img_bin, background=0)

    total_area = 0
    counter = 0
    the_biggest_component = 0

    for region in regionprops(blobs_labels):
        if region.area > 10:
            total_area += region.area
            counter += 1
        if region.area > the_biggest_component:
            the_biggest_component = region.area

    if counter == 0:
        raise ValueError("No significant components found in the image")

    average_area = total_area / counter

    small_size_threshold = ((average_area / 84) * 250) + 100
    large_size_threshold = small_size_threshold * 18

    cleaned = morphology.remove_small_objects(blobs_labels, small_size_threshold)

    component_sizes = np.bincount(cleaned.ravel())
    too_large = component_sizes > large_size_threshold
    too_large_mask = too_large[cleaned]
    cleaned[too_large_mask] = 0

    result = (cleaned > 0).astype('uint8') * 255

    output_path = os.path.join(output_dir, os.path.basename(input_path))
    cv2.imwrite(output_path, result)

    return result
