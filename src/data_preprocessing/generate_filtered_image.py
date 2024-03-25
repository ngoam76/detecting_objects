import cv2
import numpy as np
import os

# collect images from our application with the drawn polygon
# filter the images, in which we cut out the area outside the polygon
# masking with polygon

def calculate_bounding_box(center_lat, center_lon, zoom_level, image_width, image_height):
    R = 6378137
    # Calculate distance covered by one pixel in latitude and longitude
    pixel_distance_lat = 2 * np.pi * R / ( 2 ** zoom_level * 256)
    pixel_distance_lon = 2 * np.pi * R / ( 2 ** zoom_level * 256)
    pixel_distance_lat *= 0.7
    # Calculate half of the image width and height in latitude and longitude
    half_width_lat = (image_width / 2) * pixel_distance_lat
    half_height_lon = (image_height / 2) * pixel_distance_lon
    # Calculate bounding box coordinates
    min_lat = center_lat - (half_width_lat / 111319.9)
    max_lat = center_lat + (half_width_lat / 111319.9)
    min_lon = center_lon - (half_height_lon / 111319.9)
    max_lon = center_lon + (half_height_lon / 111319.9)

    return min_lat, max_lat, min_lon, max_lon

def global_to_pixel_coordinates(global_coords, image_shape, min_lat, max_lat, min_lon, max_lon):
    # Extract global coordinates
    lat, lon = global_coords
    # Calculate x coordinate (longitude)
    y = int((lon - min_lon) / (max_lon - min_lon) * (image_shape[0] - 1))
    # Calculate y coordinate (latitude)
    x = int((max_lat - lat) / (max_lat - min_lat) * (image_shape[1] - 1))

    return y,x

def filter_area_outside_polygon(image, polygon_vertices):
    mask = np.zeros_like(image, dtype=np.uint8) # creates a binary mask image with the same dimensions as the input image, the mask is initialized as an array of zeros
    cv2.fillPoly(mask, [polygon_vertices], (255, 255, 255)) # fills the polygon defined by the given polygon_vertices with white color in the mask image
    masked_image = cv2.bitwise_and(image, mask) # performs a bitwise AND operation between the input image and the mask image => retains only non-zero pixels

    return masked_image

def generate_filtered_image(input_image_path, polygon_vertices, index):
    image = cv2.imread(input_image_path)
    filtered_image = filter_area_outside_polygon(image, polygon_vertices)
    # Construct the filename based on the index
    filename = f"filtered_image_{index}.jpg"
    # Construct the full path to save the filtered image
    output_path = os.path.join(r"C:\Users\Chau Nguyen Ai Bao\OneDrive\Documents\Python\Python projects\detecting_objects\data\processed", filename)
    # Save the filtered image
    return cv2.imwrite(output_path, filtered_image)

input_image_path = r"C:\Users\Chau Nguyen Ai Bao\OneDrive\Documents\Python\Python projects\detecting_objects\data\raw\staticmap_test2.png"
polygon_vertices = np.array([(265, 325), (251, 295), (267, 355), (437, 275)], dtype=np.int32)

generate_filtered_image(input_image_path,polygon_vertices,2)
# annotate the filtered images with bounding boxes or segmentation masks to label the vegetation areas within the polygon
# preprocess the annotated images (resizing, normalization, and splitting into training and validation sets...)
# use the preprocessed images as dataset to train model - semantic segmentation model
# Evaluation performance on a separate validation set
# Inference: Apply the trained model to incoming images from users
