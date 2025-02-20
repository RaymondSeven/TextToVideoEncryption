
# **TextToVideoEncryption**  
**Secure Text-to-Video and Video-to-Text Conversion System**  

## **Overview**  
TextToVideoEncryption is a system designed to convert text into video for secure data storage and retrieval. It enables users to encode sensitive textual information into video frames and later decode it back into text. The project ensures secure, structured, and efficient storage of data through binary transformation and video encoding.  

This system is currently under **active development**, and certain features may be incomplete or require further optimization.  

---

## **Features**  

### **Text-to-Video Conversion**  
- Converts text into binary representation.  
- Maps binary data to image frames.  
- Encodes frames into an AVI/MP4 video file for secure storage.  

### **Video-to-Text Conversion**  
- Extracts frames from a video.  
- Converts image frames back into binary format.  
- Reconstructs text from the extracted binary sequence.  

### **User Interface**  
- Interactive file selection using a graphical interface.  
- Allows users to select an output directory for processed files.  
- Supports both text and video files as input.  

### **Security and Integrity**  
- Encodes text in an encrypted format within a video.  
- Provides a structured way to store and retrieve sensitive data.  
- Converts video files from AVI to MP4 for broader compatibility.  

---

## **System Requirements**  
- **Operating System:** Ubuntu/Linux (Preferred) or Windows with Python and OpenCV installed.  
- **Python Version:** Python 3.8+  
- **Dependencies:** OpenCV, NumPy, FFmpeg, and Tkinter for GUI interactions.  

---

## **Installation**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/RaymondSeven/TextToVideoEncryption.git
cd TextToVideoEncryption
```

### **2. Set Up a Virtual Environment**  
```bash
python3 -m venv .venv
source .venv/bin/activate   # On Linux/macOS
# OR
.venv\Scripts\activate      # On Windows
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Ensure FFmpeg is Installed**  
On Ubuntu:  
```bash
sudo apt update && sudo apt install ffmpeg
```
On Windows:  
1. Download **FFmpeg** from [ffmpeg.org](https://ffmpeg.org/download.html).  
2. Add FFmpeg to the system PATH.  

---

## **Usage Instructions**  

### **Running the Application**  
To start the program, run:  
```bash
python3 main.py
```

The system provides an interactive **graphical interface** where the user selects a file and an output directory.

### **File Selection**  
1. **Text File (.txt):** Converts text into a video.  
2. **Video File (.avi/.mp4):** Extracts text from the video.  

The system will process the file and save the output in the selected directory.

---

## **Project Structure**  

```
TextToVideoEncryption/
│
├── text_to_binary/
│   ├── text_to_binary.py  # Converts text to binary
│
├── binary_to_frames/
│   ├── binary_to_frames.py  # Converts binary data into frames
│
├── frames_to_video/
│   ├── frames_to_video.py  # Converts frames into video
│
├── video_to_text/
│   ├── video_to_text.py  # Extracts text from video
│
├── storage/
│   ├── video_storage.py  # Handles secure video storage
│
├── utils/
│   ├── helper_functions.py  # Helper utilities
│
├── data/
│   ├── Sample input/output files
│
├── main.py  # Entry point for the system
├── README.md  # Project documentation
├── .gitignore  # Ignores unnecessary files
└── requirements.txt  # Required dependencies
```

---

## **Technical Details**  

### **Text-to-Video Process**
1. Convert text into an **8-bit ASCII binary format**.  
2. Map binary data to pixels in an **image frame** (white for 1, black for 0).  
3. Save the frames as PNG images.  
4. Encode the frames into an AVI/MP4 **video file** using OpenCV.  

### **Video-to-Text Process**  
1. Extract frames from the video file using FFmpeg.  
2. Convert pixel data back into **binary format**.  
3. Reconstruct the original text from the binary sequence.  

---

## **Known Issues & Limitations**  
- Some **video files** may not be supported due to codec compatibility.  
- The **binary encoding process** may need optimization for larger text files.  
- The **current playback format** (AVI) may not be compatible with all media players.  
- **Graphical UI** is minimal and needs refinement.  

---

## **Future Enhancements**  
- Improve the efficiency of the **binary-to-frame mapping**.  
- Support for **additional video formats** and compression techniques.  
- Implement a **stronger encryption mechanism** for secure encoding.  
- Develop a **web-based interface** for easier use.  

---

## **Contributing**  
Contributions are welcome! If you find bugs or have suggestions, feel free to **open an issue** or **submit a pull request**.  

1. **Fork the repository**  
2. **Create a feature branch:**  
   ```bash
   git checkout -b feature-name
   ```
3. **Commit your changes:**  
   ```bash
   git commit -m "Added new feature"
   ```
4. **Push to GitHub:**  
   ```bash
   git push origin feature-name
   ```
5. **Create a Pull Request**  

---

## **License**  
This project is licensed under the **MIT License**.  

---

## **Contact**  
For any issues, suggestions, or contributions, please contact the project owner via GitHub.

---
