# ai-test

A project featuring an audio visualizer and ManimGL (Manim v2) for creating programmatic animations.

## Features

- **Audio Visualizer**: Browser-based audio visualization with multiple modes (bars, wave, circle)
- **ManimGL Integration**: Create mathematical animations using 3Blue1Brown's Manim engine

## Audio Visualizer

Open `index.html` in a browser to use the audio visualizer. Supports:
- Loading audio files
- Microphone input
- Three visualization modes

## ManimGL Setup

### Prerequisites

- Python 3.7+
- FFmpeg
- OpenGL
- LaTeX (optional, for mathematical equations)

### Linux Additional Requirements

```bash
sudo apt install libpango1.0-dev pkg-config python3-dev
```

### macOS Additional Requirements

```bash
brew install ffmpeg pango pkg-config
```

### Installation

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or
venv\Scripts\activate     # Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Running Example Scenes

```bash
# Hello World scene
manimgl scenes/example_scenes.py HelloWorld

# Basic shapes demonstration
manimgl scenes/example_scenes.py BasicShapes

# Mathematical equations
manimgl scenes/example_scenes.py MathEquations

# Wave animation
manimgl scenes/example_scenes.py WaveAnimation

# 3D surface demonstration
manimgl scenes/example_scenes.py ThreeDScene

# Interactive demo
manimgl scenes/example_scenes.py InteractiveDemo
```

### Useful Flags

- `-w`: Write to file (saves video)
- `-o`: Write to file and open
- `-s`: Skip to the end and show final frame
- `-f`: Full screen preview
- `-n <number>`: Start at animation number
- `-a`: Run all scenes

Example:
```bash
manimgl scenes/example_scenes.py HelloWorld -w
```

### Project Structure

```
ai-test/
├── index.html          # Audio visualizer
├── requirements.txt    # Python dependencies
├── custom_config.py    # ManimGL configuration
├── scenes/
│   └── example_scenes.py  # Example Manim scenes
└── media/              # Generated videos (after rendering)
```

## Resources

- [ManimGL Documentation](https://3b1b.github.io/manim/)
- [ManimGL GitHub](https://github.com/3b1b/manim)
- [3Blue1Brown YouTube](https://www.youtube.com/c/3blue1brown)
