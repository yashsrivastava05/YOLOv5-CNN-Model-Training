import os
import subprocess
from pathlib import Path

# Function to train YOLOv5 with multiple classes
def train_yolov5(data_yaml, weights="yolov5m.pt", img_size=416, batch_size=16, epochs=50, device=0, project_path="/drive/MyDrive/new0yolo/weights/new_weights"):
    """
    Trains YOLOv5 using specified parameters for a multi-class dataset.
    """
    command = [
        "python", "/content/yolov5/train.py",  # Path to YOLOv5's train script
        "--img", str(img_size),
        "--batch", str(batch_size),
        "--epochs", str(epochs),
        "--data", "/drive/MyDrive/new0yolo/newDATASET/dataset.yaml",  # Path to dataset.yaml
        "--weights", weights,  # Pretrained weights
        "--device", str(device), #for gpu str(device) for cpu "cpu" 
        "--project", project_path
    ]
    subprocess.run(command, check=True)

# Check paths and dataset configuration
def validate_paths():
    yaml_path = Path('/drive/MyDrive/new0yolo/newDATASET/dataset.yaml')
    train_dir = Path('/drive/MyDrive/new0yolo/newDATASET/train')
    val_dir = Path('/drive/MyDrive/new0yolo/newDATASET/val')

    if not yaml_path.exists():
        raise FileNotFoundError(f"Dataset YAML not found at {yaml_path}")
    if not train_dir.exists():
        raise FileNotFoundError(f"Training directory not found at {train_dir}")
    if not val_dir.exists():
        raise FileNotFoundError(f"Validation directory not found at {val_dir}")

    print("All dataset paths validated successfully.")

# Validate dataset paths
validate_paths()

# Train YOLOv5 for multiple classes
data_yaml = "/drive/MyDrive/new0yolo/newDATASET/dataset.yaml"  # Ensure the dataset.yaml is configured correctly
hyp_path = 
train_yolov5(data_yaml)

# Dataset.yaml Example Configuration:
# train: "/drive/MyDrive/new0yolo/newDATASET/train"  # Path to train images and labels
# val: "/drive/MyDrive/new0yolo/newDATASET/val"    # Path to validation images and labels
# nc: 6  # Number of classes
# names: ['id_card', 'logo', 'college', 'valid', 'info', 'key']  # List of class names
