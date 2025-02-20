import os
import shutil

def store_video(video_path: str, storage_folder: str):
    """
    Stores the encrypted video securely in a storage directory.
    """
    if not os.path.exists(storage_folder):
        os.makedirs(storage_folder)
    
    filename = os.path.basename(video_path)
    stored_path = os.path.join(storage_folder, filename)
    
    shutil.move(video_path, stored_path)
    os.chmod(stored_path, 0o600)
    print(f"Video securely stored at {stored_path}")

def list_stored_videos(storage_folder: str):
    """
    Lists all stored video files.
    """
    if not os.path.exists(storage_folder):
        print("Storage folder does not exist.")
        return []
    
    videos = [file for file in os.listdir(storage_folder) if file.endswith(".mp4")]
    return videos

def main():
    """
    Main function to store and list encrypted videos.
    """
    video_path = "../data/output_video.mp4"
    storage_folder = "../data/secure_storage/"
    
    store_video(video_path, storage_folder)
    
    print("Stored Videos:")
    print(list_stored_videos(storage_folder))

if __name__ == "__main__":
    main()
