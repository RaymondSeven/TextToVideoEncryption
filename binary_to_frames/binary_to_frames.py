import os
import numpy as np
import cv2

def binary_to_image(binary_data: str, output_image_path: str, width: int = 256, height: int = 256):
    """
    Converts binary data into an image frame.
    """
    binary_list = [int(bit) for bit in binary_data]
    total_pixels = width * height

    binary_list += [0] * (total_pixels - len(binary_list))
    binary_array = np.array(binary_list[:total_pixels], dtype=np.uint8).reshape((height, width)) * 255

    cv2.imwrite(output_image_path, binary_array)
    print(f"✅ Image saved to {output_image_path} with size {width}x{height}")

def load_binary_from_file(input_path: str) -> str:
    """
    Loads binary data from a file.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Binary file {input_path} not found.")
    
    with open(input_path, 'r') as file:
        return file.read().strip()

def main():
    """
    Main function to convert binary data into an image.
    """
    base_path = os.path.dirname(os.path.abspath(__file__))
    binary_file = os.path.join(base_path, "../data/binary_data.txt")  
    frames_folder = os.path.join(base_path, "../data/frames/")  
    os.makedirs(frames_folder, exist_ok=True)
    output_image = os.path.join(frames_folder, "frame_0.png")  

    binary_data = load_binary_from_file(binary_file)
    binary_to_image(binary_data, output_image)

if __name__ == "__main__":
    main()
