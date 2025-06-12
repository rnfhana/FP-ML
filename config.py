"""
Configuration file for Waste Classification Streamlit App
"""

import os
from pathlib import Path

# App Configuration
APP_TITLE = "Smart Waste Classifier"
APP_ICON = "♻️"
PAGE_LAYOUT = "wide"

# Model Configuration
MODEL_PATH = "my_model.pkl"
MODEL_ARCHITECTURE = "ResNet34"
INPUT_SIZE = (224, 224)
BATCH_SIZE = 32

# Waste Categories
WASTE_CATEGORIES = [
    "cardboard",
    "glass", 
    "metal",
    "paper",
    "plastic"
]

# Category Display Names
CATEGORY_DISPLAY_NAMES = {
    "cardboard": "Cardboard",
    "glass": "Glass",
    "metal": "Metal", 
    "paper": "Paper",
    "plastic": "Plastic"
}

# Category Emojis
CATEGORY_EMOJIS = {
    "cardboard": "♻️",
    "glass": "🍶",
    "metal": "🔩",
    "paper": "📄",
    "plastic": "🥤"
}

# File Upload Settings
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB in bytes
MAX_IMAGE_DIMENSION = 2048

# UI Colors
COLORS = {
    "primary": "#667eea",
    "secondary": "#764ba2", 
    "success": "#84fab0",
    "warning": "#ffecd2",
    "danger": "#ff9a9e",
    "light": "#a8edea",
    "dark": "#2c3e50"
}

# Confidence Thresholds
CONFIDENCE_THRESHOLDS = {
    "high": 0.8,
    "medium": 0.6,
    "low": 0.4
}

# Performance Metrics (Demo Data)
DEMO_METRICS = {
    "overall_accuracy": 0.952,
    "overall_f1": 0.949,
    "class_metrics": {
        "cardboard": {"precision": 0.94, "recall": 0.95, "f1": 0.945},
        "glass": {"precision": 0.89, "recall": 0.90, "f1": 0.895},
        "metal": {"precision": 0.91, "recall": 0.92, "f1": 0.915},
        "paper": {"precision": 0.96, "recall": 0.94, "f1": 0.950},
        "plastic": {"precision": 0.98, "recall": 0.97, "f1": 0.975}
    }
}

# Training Configuration (for display purposes)
TRAINING_CONFIG = {
    "epochs": 15,
    "learning_rate": 1e-3,
    "batch_size": 32,
    "data_split": {
        "train": 0.8,
        "validation": 0.1,
        "test": 0.1
    },
    "augmentation": {
        "horizontal_flip": True,
        "vertical_flip": False,
        "max_rotate": 20,
        "max_zoom": 1.1,
        "max_lighting": 0.3
    }
}

# Paths
BASE_DIR = Path(__file__).parent
MODEL_DIR = BASE_DIR / "models"
DATA_DIR = BASE_DIR / "data"
STATIC_DIR = BASE_DIR / "static"
TEMP_DIR = BASE_DIR / "temp"

# Create directories if they don't exist
for directory in [MODEL_DIR, DATA_DIR, STATIC_DIR, TEMP_DIR]:
    directory.mkdir(exist_ok=True)

# Environment Variables
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
PORT = int(os.getenv("PORT", 8501))

# Logging Configuration
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
        },
    },
    "handlers": {
        "default": {
            "level": "INFO",
            "formatter": "standard",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "": {
            "handlers": ["default"],
            "level": "INFO",
            "propagate": False
        }
    }
}

# Cache Configuration
CACHE_CONFIG = {
    "model_cache_ttl": 3600,  # 1 hour
    "data_cache_ttl": 1800,   # 30 minutes
    "max_cache_entries": 100
}

# Error Messages
ERROR_MESSAGES = {
    "model_not_found": "Model file not found. Please ensure 'my_model.pkl' is in the correct directory.",
    "invalid_image": "Invalid image file. Please upload a valid PNG, JPG, or JPEG image.",
    "file_too_large": f"File too large. Maximum size allowed is {MAX_FILE_SIZE // (1024*1024)}MB.",
    "prediction_error": "Error occurred during prediction. Please try again.",
    "upload_error": "Error uploading file. Please try again."
}

# Success Messages
SUCCESS_MESSAGES = {
    "model_loaded": "Model loaded successfully!",
    "prediction_complete": "Prediction completed successfully!",
    "file_uploaded": "File uploaded successfully!"
}

# Info Messages
INFO_MESSAGES = {
    "model_loading": "Loading model, please wait...",
    "processing_image": "Processing image...",
    "making_prediction": "Making prediction..."
}