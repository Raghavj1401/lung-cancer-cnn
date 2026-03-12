# Lung Cancer Detection using CNN

A deep learning project that detects lung cancer types from CT scan images using a **Convolutional Neural Network (CNN)**.  
The model is trained using TensorFlow/Keras and deployed through a **Streamlit web application** for easy interaction.

---

## Project Overview

Lung cancer is one of the leading causes of cancer-related deaths worldwide. Early detection plays a crucial role in improving patient survival rates.  

This project builds a **CNN-based image classification model** that analyzes CT scan images and predicts the type of lung cancer.

The application allows users to **upload a CT scan image** and receive a predicted cancer type along with a confidence score.

---

## Dataset

The dataset contains CT scan images categorized into **four classes**:

- Adenocarcinoma
- Large Cell Carcinoma
- Squamous Cell Carcinoma
- Normal

The dataset is divided into:

- **Training Set**
- **Validation Set**
- **Test Set**

Dataset structure:


data/
└── Lung Cancer Detection Dataset
├── train
│ ├── adenocarcinoma
│ ├── large_cell
│ ├── normal
│ └── squamous
├── valid
│ ├── adenocarcinoma
│ ├── large_cell
│ ├── normal
│ └── squamous
└── test
├── adenocarcinoma
├── large_cell
├── normal
└── squamous


⚠️ The dataset is **not included in this repository** due to size limitations.

---

## Model Architecture

The Convolutional Neural Network consists of:

- Convolution Layers – extract image features
- MaxPooling Layers – reduce spatial dimensions
- Flatten Layer – convert feature maps into a 1D vector
- Dense Layers – perform classification
- Softmax Output Layer – outputs probabilities for the four classes

---

## Model Performance

After training the model:

| Metric | Value |
|------|------|
| Training Accuracy | ~96% |
| Validation Accuracy | ~94–100% |
| Test Accuracy | ~93–100% |

These results indicate that the CNN model performs well in classifying lung CT scan images.

---

## Streamlit Web Application

A **Streamlit frontend interface** was developed to make the model interactive.

Features:

- Upload CT scan image
- Model predicts cancer type
- Displays prediction confidence
- Visualization of prediction probabilities

Example workflow:

1. Upload CT scan image
2. Model processes the image
3. Prediction result is displayed

---

## Project Structure


lung-cancer-cnn/
│
├── notebooks/
│ └── lung_cancer_training.ipynb
│
├── models/
│ └── lung_cancer_cnn.h5
│
├── data/
│ └── Lung Cancer Detection Dataset
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore


---

## Installation

Clone the repository:

```bash
git clone https://github.com/Raghavj1401/lung-cancer-cnn.git
cd lung-cancer-cnn

Install dependencies:

pip install -r requirements.txt
Run the Streamlit App
streamlit run app.py

Then open the provided local URL in your browser.

Technologies Used

Python

TensorFlow / Keras

NumPy

Matplotlib

Streamlit

Future Improvements

Use a larger dataset

Apply transfer learning (ResNet / EfficientNet)

Improve model generalization

Deploy the application online

Author

Raghav
B.Tech Electrical Engineering

License

This project is for educational and research purposes.
