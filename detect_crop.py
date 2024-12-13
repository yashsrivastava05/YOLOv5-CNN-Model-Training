import torch
import cv2
import os
#fhjfjfjffyf
def detect_and_crop(model_path, source_folder, output_folder):
    """
    Detect objects in images using a trained YOLOv5 model and crop them.
    """
    # Load YOLOv5 model
    model = torch.hub.load("ultralytics/yolov5", "custom", path=model_path, force_reload=True)
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through images in the source folder
    for img_file in os.listdir(source_folder):
        if img_file.endswith(('.jpg', '.png', '.jpeg')):
            img_path = os.path.join(source_folder, img_file)

            # Run inference
            results = model(img_path)

            # Extract bounding boxes and labels
            for i, (xmin, ymin, xmax, ymax, conf, cls) in enumerate(results.xyxy[0].cpu().numpy()):
                class_name = results.names[int(cls)]
                print(f"Detected {class_name} at [{xmin}, {ymin}, {xmax}, {ymax}] with confidence {conf}")

                # Read and crop the image
                image = cv2.imread(img_path)
                cropped = image[int(ymin):int(ymax), int(xmin):int(xmax)]

                # Save the cropped image
                crop_filename = f"{os.path.splitext(img_file)[0]}_crop_{i}_{class_name}.jpg"
                crop_path = os.path.join(output_folder, crop_filename)
                cv2.imwrite(crop_path, cropped)
                print(f"Saved cropped image: {crop_path}")

# Paths
model_path = "/drive/MyDrive/Yolo_saved_traning_data/best.pt"  # Path to trained model weights
source_folder = "/drive/MyDrive/Test_image"  # Folder containing test images
output_folder = "/content/drive/MyDrive/cropped_objects"  # Folder for saving cropped objects

# Detect and crop
detect_and_crop(model_path, source_folder, output_folder)
