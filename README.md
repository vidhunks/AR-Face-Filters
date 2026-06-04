# AR Face Filters 🎭

A real-time augmented reality (AR) face filter application that uses MediaPipe for face detection and OpenCV for rendering. Apply fun filters like glasses, mustaches, and cat ears to your face via webcam.

## Features ✨

- **Multiple Filters**: Choose from several AR filters to apply to your face:
  - 👓 Glasses
  - 👨 Mustache
  - 🎭 Both (Glasses + Mustache)
  - 🐱 Cat Ears
  - ⊘ No Filter

- **Real-Time Processing**: Uses MediaPipe's FaceMesh for fast and accurate face landmark detection
- **Easy Filter Switching**: Switch between filters using keyboard shortcuts (0, 1, 2, 3, 4)
- **High-Quality Rendering**: Smooth alpha blending for natural-looking overlays

## Prerequisites 📋

- Python 3.x
- Webcam

## Installation 🔧

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vidhunks/AR-Face-Filters.git
   cd AR-Face-Filters
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Dependencies 📦

The project requires the following Python packages:

- **mediapipe** (0.10.14) - For face mesh detection
- **numpy** (1.26.4) - For numerical operations
- **opencv-contrib-python** (4.10.0.84) - For computer vision tasks
- **protobuf** (4.25.3) - For protocol buffer serialization
- **absl-py** (2.1.0) - For abseil Python utilities

## Usage 🚀

Run the main application:

```bash
cd src
python main.py
```

### Keyboard Controls

| Key | Action |
|-----|--------|
| `1` | Apply Glasses filter |
| `2` | Apply Mustache filter |
| `3` | Apply Both (Glasses + Mustache) |
| `4` | Apply Cat Ears filter |
| `0` | Remove all filters |
| `q` | Quit the application |

## Project Structure 📂

```
AR-Face-Filters/
├── src/
│   ├── main.py                 # Main application entry point
│   ├── check_mediapipe.py      # MediaPipe verification script
│   ├── detector/
│   │   ├── face_detector.py    # Face detection module
│   │   └── face_mesh_detector.py # Face mesh detection using MediaPipe
│   ├── filters/
│   │   ├── glass_filter.py     # Glasses filter implementation
│   │   ├── mustache_filter.py  # Mustache filter implementation
│   │   └── cat_filter.py       # Cat ears filter implementation
│   └── utils/
│       ├── overlay.py          # PNG overlay utility functions
│       └── helpers.py          # Helper functions
├── assets/                     # Filter images (PNG files with transparency)
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
└── README.md                   # This file
```

## How It Works 🔍

### Face Detection (`FaceMeshDetector`)
- Uses MediaPipe's FaceMesh solution to detect facial landmarks in real-time
- Returns 468 landmark points on the face with high accuracy
- Processes video frames with configurable confidence thresholds

### Filter Application
Each filter (glasses, mustache, cat ears) follows this workflow:

1. **Landmark Detection**: Extract specific facial landmarks from FaceMesh results
2. **Positioning**: Calculate filter position and size based on face dimensions
3. **Resizing**: Resize the filter PNG to fit the detected face features
4. **Overlay**: Blend the filter with the video frame using alpha transparency

### Alpha Blending (`overlay_png`)
- Handles transparent PNG overlays with per-pixel alpha channels
- Blends overlay with background using alpha-compositing formula
- Handles edge cases where overlays extend beyond frame boundaries

## Key Components 🔌

### `FaceMeshDetector`
Initializes and uses MediaPipe's FaceMesh solution for face landmark detection.

```python
detector = FaceMeshDetector()
results = detector.detect_mesh(frame)
```

### Filter Classes
Each filter class (GlassFilter, MustacheFilter, CatFilter) implements:
- `__init__`: Load filter image asset
- `apply(frame, face_landmarks)`: Apply filter to frame using face landmarks

### `overlay_png` Function
Handles transparent PNG rendering with:
- Boundary checking
- Alpha channel blending
- Performance optimization

## File Format

Filter assets should be PNG files with transparency (RGBA format):
- **glasses.png**: Positioned between the eyes
- Other filter assets stored in the `assets/` directory

## Future Enhancements 🚀

- Add more filter designs (hats, masks, etc.)
- Support for multiple faces simultaneously
- Video recording with applied filters
- Filter customization options
- Performance optimizations for lower-end devices
- Face expression recognition

## Troubleshooting 🔧

**MediaPipe not found**: Ensure MediaPipe is properly installed:
```bash
pip install --upgrade mediapipe
```

**Webcam not accessible**: Check if your webcam is:
- Properly connected
- Not in use by other applications
- Has proper OS permissions granted

**Filters not appearing**: Verify that:
- Asset PNG files exist in the `assets/` directory
- PNG files have proper RGBA format with transparency
- Landmark indices match the MediaPipe FaceMesh specification

## License 📄

This project is open source. Feel free to fork, modify, and use it as needed.

## Contributing 🤝

Contributions are welcome! Feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests with improvements

## Author 👤

Created by [@vidhunks](https://github.com/vidhunks)

---

**Enjoy applying AR filters to your face! 🎉**
