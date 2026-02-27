# ManimGL Custom Configuration
# This file allows you to customize default ManimGL settings

from manimlib import *

# Directory configurations
MEDIA_DIR = "./media"
VIDEO_DIR = f"{MEDIA_DIR}/videos"
IMAGES_DIR = f"{MEDIA_DIR}/images"

# Default resolution settings
DEFAULT_PIXEL_HEIGHT = 1080
DEFAULT_PIXEL_WIDTH = 1920
DEFAULT_FRAME_RATE = 60

# Camera settings
FRAME_HEIGHT = 8.0
FRAME_WIDTH = FRAME_HEIGHT * DEFAULT_PIXEL_WIDTH / DEFAULT_PIXEL_HEIGHT

# Color scheme (can be customized)
BACKGROUND_COLOR = "#1a1a2e"  # Matches the audio visualizer theme
