import os
import cv2
import numpy as np

def ensure_directory_exists(directory_path):
    """Creates the directory if it does not exist."""
    os.makedirs(directory_path, exist_ok=True)

def save_image(image, path):
    """Saves an image to the specified path."""
    cv2.imwrite(path, image)

def load_image(image_path, grayscale=True):
    """Loads an image from the specified path."""
    if grayscale:
        return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    return cv2.imread(image_path, cv2.IMREAD_COLOR)

def list_files_in_directory(directory, extension=None):
    """Lists files in a directory with an optional extension filter."""
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if extension:
        files = [f for f in files if f.lower().endswith(extension)]
    return files

def convert_avi_to_mp4(input_avi, output_mp4):
    """Converts an AVI file to MP4 format using ffmpeg."""
    os.system(f"ffmpeg -i \"{input_avi}\" -c:v libx264 -preset slow -b:v 1000k -r 10 -pix_fmt yuv420p \"{output_mp4}\"")
