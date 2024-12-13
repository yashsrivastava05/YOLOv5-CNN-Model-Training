# **ID Card Detection System**

## **Overview**
The **ID Card Detection System** is an AI-powered solution designed to automate attendance management. It uses advanced object detection and machine learning techniques to recognize and extract key details (e.g., name, ID number) from college ID cards in real time. This system, developed for Maharana Pratap Group of Institutions, simplifies attendance tracking, reduces manual errors, and improves operational efficiency.

---

## **Technologies Used**
- **Object Detection Model:** YOLOv5  
- **Programming Language:** Python  
- **Annotation Tool:** LabelImg  
- **Development Environment:** Google Colab with 16GB TPU  
- **Database:** MongoDB (for storing extracted data)  

---

## **How It Works**
1. **Dataset Preparation**  
   - Collected and annotated a custom dataset of over 1,000 ID card images using LabelImg.  
   - Annotations were used to define bounding boxes for effective object detection.  

2. **Model Training**  
   - Trained the YOLOv5 object detection model on the annotated dataset using Google Colab.  
   - Leveraged a 16GB TPU for high-speed computation, achieving over 90% detection accuracy.  

3. **Real-Time Detection and Attendance**  
   - The system detects ID cards in real time, extracts relevant details, and marks attendance by integrating with a backend database.  
   - Eliminates manual errors and ensures accurate attendance tracking.  

---

## **Features and Benefits**
- **High Accuracy:** Achieves over 90% detection reliability for ID card recognition.  
- **Automation:** Reduces manual workload and streamlines attendance processes.  
- **Scalability:** Adaptable for broader applications like event or corporate attendance systems.  

---

