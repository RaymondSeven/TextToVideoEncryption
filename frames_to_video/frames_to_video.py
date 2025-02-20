import os
import cv2

def images_to_video(frame_folder: str, output_video_path: str, frame_rate: int = 10):
    """
    Combines image frames into a video.
    """
    images = [img for img in sorted(os.listdir(frame_folder)) if img.endswith(".png")]

    if not images:
        raise FileNotFoundError("❌ No frames found in the specified directory. Check if Step 2 (Binary to Frames) ran correctly.")

    print(f"✅ Frames found: {images}")

    frame_path = os.path.join(frame_folder, images[0])
    frame = cv2.imread(frame_path)

    if frame is None:
        raise ValueError(f"❌ Failed to read the first frame: {frame_path}")

    height, width, _ = frame.shape
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # Changed codec to XVID
    print(f"🔍 FOURCC: {fourcc}, Frame Size: {width}x{height}, Frame Rate: {frame_rate}")

    video = cv2.VideoWriter(output_video_path, fourcc, frame_rate, (width, height))

    if not video.isOpened():
        raise RuntimeError("❌ OpenCV VideoWriter failed to open. Check codec and permissions!")

    for image in images:
        frame = cv2.imread(os.path.join(frame_folder, image))
        if frame is None:
            print(f"⚠️ Warning: Skipping unreadable frame {image}")
            continue
        print(f"📝 Writing frame: {image}")
        video.write(frame)

    video.release()

    # Verify file creation
    if not os.path.exists(output_video_path):
        raise FileNotFoundError(f"❌ Video file {output_video_path} was not created!")

    print(f"✅ Video successfully saved to {output_video_path}")

if __name__ == "__main__":
    frame_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/frames/")
    output_video_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/output_video.avi")

    
    print("🔄 Running Video Encoding Process...")
    images_to_video(frame_folder, output_video_path)
    print("✅ Video encoding complete.")
