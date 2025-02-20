import os
import numpy as np
import cv2
import tkinter as tk
from tkinter import filedialog
from text_to_binary.text_to_binary import text_to_binary, load_text_from_file, save_binary_to_file
from binary_to_frames.binary_to_frames import binary_to_image, load_binary_from_file
from frames_to_video.frames_to_video import images_to_video
from video_to_text.video_to_text import frames_to_binary, save_text_from_binary

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a File to Process", filetypes=[
        ("Text Files", "*.txt"),
        ("Video Files", "*.avi;*.mp4")
    ])
    return file_path

def select_output_directory():
    root = tk.Tk()
    root.withdraw()
    output_dir = filedialog.askdirectory(title="Select Output Directory")
    return output_dir

def convert_avi_to_mp4(input_avi, output_dir):
    """Converts AVI video to MP4 format."""
    mp4_output_file = os.path.join(output_dir, "output_video.mp4")
    os.system(f"ffmpeg -i \"{input_avi}\" -c:v libx264 -preset slow -b:v 1000k -r 10 -pix_fmt yuv420p \"{mp4_output_file}\"")
    print(f"Converted AVI to MP4: {mp4_output_file}")
    return mp4_output_file

def process_text_to_video(input_text_file, output_dir):
    """Handles text-to-video conversion"""
    print("Converting Text to Video...")
    video_output_file = os.path.join(output_dir, "output_video.avi")
    
    text = load_text_from_file(input_text_file)
    binary_data = text_to_binary(text)
    
    frame_output_folder = os.path.join(output_dir, "frames/")
    os.makedirs(frame_output_folder, exist_ok=True)
    output_image = os.path.join(frame_output_folder, "frame_0.png")
    binary_to_image(binary_data, output_image)
    
    images_to_video(frame_output_folder, video_output_file)
    print(f"Video saved to {video_output_file}")
    
    convert_avi_to_mp4(video_output_file, output_dir)

def process_video_to_text(input_video_file, output_dir):
    """Handles video-to-text conversion"""
    print("Converting Video to Text...")
    reconstructed_text_file = os.path.join(output_dir, "reconstructed_text.txt")
    
    extracted_frames_folder = os.path.join(output_dir, "extracted_frames/")
    os.makedirs(extracted_frames_folder, exist_ok=True)
    os.system(f"ffmpeg -i \"{input_video_file}\" \"{extracted_frames_folder}/frame_%04d.png\"")
    
    binary_data = frames_to_binary(extracted_frames_folder)
    save_text_from_binary(binary_data, reconstructed_text_file)
    print(f"Reconstructed text saved to {reconstructed_text_file}")

def main():
    print("Welcome to the Text-to-Video Encryption System!")
    print("Please select a file to process:")
    file_path = select_file()
    
    if not file_path:
        print("No file selected. Exiting...")
        return
    
    print("Please select an output directory:")
    output_dir = select_output_directory()
    
    if not output_dir:
        print("No output directory selected. Exiting...")
        return
    
    file_ext = os.path.splitext(file_path)[1].lower()
    
    if file_ext == ".txt":
        process_text_to_video(file_path, output_dir)
    elif file_ext in [".avi", ".mp4"]:
        process_video_to_text(file_path, output_dir)
    else:
        print("Unsupported file type. Please select a .txt or .avi/.mp4 file.")
        return
    
    print(f"Process Complete! Check the output in {output_dir}")
    
if __name__ == "__main__":
    main()
