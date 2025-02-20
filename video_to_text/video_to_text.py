import os
import cv2
import numpy as np

def frames_to_binary(frame_folder: str) -> str:
    """
    Converts extracted frames back into binary.
    """
    frame_folder = os.path.abspath(frame_folder)

    if not os.path.exists(frame_folder):
        raise FileNotFoundError(f"❌ Frame folder {frame_folder} does not exist!")

    images = sorted([img for img in os.listdir(frame_folder) if img.endswith(".png")])
    if not images:
        raise FileNotFoundError(f"❌ No frames found in {frame_folder}")

    binary_data = ""
    for image in images:
        image_path = os.path.join(frame_folder, image)
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            print(f"⚠️ Warning: Skipping unreadable frame {image}")
            continue

        img = (img > 127).astype(np.uint8)
        binary_data += "".join(str(bit) for bit in img.flatten())

    return binary_data

def save_text_from_binary(binary_data: str, output_text_file: str):
    """
    Converts binary data back into text and saves it.
    """
    text = "".join(chr(int(binary_data[i:i+8], 2)) for i in range(0, len(binary_data), 8))
    with open(output_text_file, "w") as file:
        file.write(text)
    print(f"✅ Reconstructed text saved to {output_text_file}")

def main():
    frame_folder = os.path.abspath("data/extracted_frames/")
    output_text_file = os.path.abspath("data/reconstructed_text.txt")

    print("🔄 Converting frames back into text...")
    binary_data = frames_to_binary(frame_folder)
    save_text_from_binary(binary_data, output_text_file)

if __name__ == "__main__":
    main()
