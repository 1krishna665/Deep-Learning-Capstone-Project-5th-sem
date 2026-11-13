# Smart Campus Indoor Scene Recognition using Deep Learning and Edge AI

## 1. Project Overview

Smart Campus Indoor Scene Recognition is a Deep Learning-based project designed to identify and classify indoor environments in a college campus. It uses the **MobileNetV3-Large** architecture to recognize six different indoor scene categories from uploaded images.

The project aims to support smart campus navigation by automatically identifying indoor locations using computer vision and Edge AI technology.

## 2. Project Objectives

- Develop an automated indoor scene recognition system.
- Classify campus environments into six categories.
- Implement a lightweight Deep Learning model using MobileNetV3-Large.
- Evaluate model performance using classification metrics.
- Deploy the trained model through a web application.
- Explore Edge AI deployment for future real-time campus applications.

## 3. Technologies Used

- Python
- PyTorch and Torchvision
- MobileNetV3-Large
- Deep Learning and Computer Vision
- Flask
- HTML, CSS and JavaScript
- Google Colab
- VS Code
- GitHub
- Cloud Deployment

## 4. Dataset

The project uses the MIT Indoor 67 dataset and a selected six-class subset.

**Target Classes:**
1. Classroom
2. Common_Canteen
3. Corridor
4. Laboratory
5. Library
6. Office

The selected dataset initially contains 800 images, divided into training and testing sets.

**Dataset Access:**  
[MIT Indoor 67 Dataset](https://web.mit.edu/torralba/www/indoor.html)

Download the dataset and organize the images according to the six target categories before training.

## 5. Model Architecture

The project uses **MobileNetV3-Large**, a lightweight Convolutional Neural Network architecture suitable for image classification and resource-efficient applications.

The model uses transfer learning with pretrained ImageNet weights. Its final classification layer is modified to predict six indoor scene categories.

**Workflow:**

1. Dataset collection and preprocessing
2. Image resizing and normalization
3. Transfer learning using MobileNetV3-Large
4. Model training and validation
5. Performance evaluation
6. Image upload and scene prediction
7. Cloud deployment

## 6. Model Performance

The reported experimental results are:

| Evaluation Metric | Result |
|---|---:|
| Top-1 Accuracy | 86.25% |
| Top-3 Accuracy | 98.12% |
| Macro F1-Score | 0.8663 |

These results represent the reported evaluation on the project's test dataset.

## 7. Project Structure

```text
Smart-Campus-Scene-Recognition/
│
├── app.py
├── requirements.txt
├── render.yaml
│
├── model/
│   └── mobilenetv3_six_class.pth
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── notebooks/
│   └── model_training.ipynb
│
├── screenshots/
│   ├── home_page.png
│   ├── image_upload.png
│   └── prediction_output.png
│
├── README.md
└── .gitignore
```

## 8. Installation and Execution

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Smart-Campus-Scene-Recognition
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Add Model Weights

Download the trained model checkpoint and place it inside the `model/` directory.

Ensure that the checkpoint filename and path match the configuration in `app.py`.

### Step 5: Run the Application

```bash
python app.py
```

### Step 6: Open the Web Application

Open the following address in your browser:

```text
http://127.0.0.1:5000
```

Upload an indoor image to receive the predicted scene category and confidence scores.

## 9. Deployment

The project is deployed as a cloud-based web application using Flask and Render.

Users can access the application through the deployed URL, upload indoor images and view classification results without running the training notebook.

**Live Application:**  
[Add Your Deployed Application URL]

## 10. Sample Outputs

The `screenshots/` directory contains examples of:

- Application home page
- Image upload interface
- Classroom recognition
- Laboratory recognition
- Corridor recognition
- Library and office predictions
- Prediction results with confidence scores

## 11. Challenges and Learnings

- Working with a limited number of training images.
- Handling visually similar indoor environments.
- Improving model generalization to real campus photographs.
- Understanding transfer learning and MobileNetV3-Large.
- Managing image preprocessing and class mapping.
- Deploying a PyTorch model using Flask and cloud services.
- Understanding the challenges of deploying Deep Learning models on resource-constrained Edge AI devices.

## 12. Future Scope

- Expand the dataset using real photographs collected from the college campus.
- Improve recognition accuracy through additional training data and fine-tuning.
- Deploy the model on NVIDIA Jetson Nano or Jetson Orin Nano.
- Develop real-time indoor scene recognition using a camera.
- Integrate the recognition system with smart campus navigation.

## 13. Team Members

| Name | Roll Number |
|---|---:|
| Krish Yadav | 27 |
| Krishna Satpute | 29 |
| Rudra Bhor | 45 |
| Omkar Umale | 35 |

## 14. Final Project Submission

The project submission includes:

- **IEEE Conference Report:** `Group ID_V-B.doc`
- **GitHub Repository:** Complete source code, model weights, dataset instructions, README and output screenshots.
- **Project ZIP:** `Group ID_V-B.ZIP`
- **Final Presentation:** `Group ID_V-B.pptx`
The final presentation contains 6–8 slides covering:
1. Title and Team Members
2. Problem Statement
3. Dataset
4. Methodology and Model Architecture
5. Experiments and Hyperparameters
6. Results
7. Challenges and Learnings
8. Conclusion and Future Work
---
## 15. Conclusion
Smart Campus Indoor Scene Recognition demonstrates the application of Deep Learning and Computer Vision for indoor environment classification. By using MobileNetV3-Large and cloud deployment, the project provides a foundation for intelligent campus navigation and future Edge AI applications.

Smart Campus Indoor Scene Recognition demonstrates the application of Deep Learning and Computer Vision for indoor environment classification. By using MobileNetV3-Large and cloud deployment, the project provides a foundation for intelligent campus navigation and future Edge AI applications.
