# Lung Cancer Detection using CNN

**Name:** Raghav Joshi  
**Registered Email:** raghavjoshi200314@gmail.com  
**Course & Batch:** PBEL 2.2 Artificial Intelligence – Batch 8  

---

## Project Overview

Lung cancer is one of the leading causes of cancer-related deaths worldwide. Early detection plays a crucial role in improving patient survival rates.

This project builds a **Convolutional Neural Network (CNN)** that analyzes **CT scan images** and predicts the type of lung cancer.

The model is trained using **TensorFlow/Keras** and integrated with a **Streamlit web application** that allows users to upload CT scan images and receive predictions.

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

### Dataset Structure

```
data/
└── Lung Cancer Detection Dataset
    ├── train
    │   ├── adenocarcinoma
    │   ├── large_cell
    │   ├── normal
    │   └── squamous
    │
    ├── valid
    │   ├── adenocarcinoma
    │   ├── large_cell
    │   ├── normal
    │   └── squamous
    │
    └── test
        ├── adenocarcinoma
        ├── large_cell
        ├── normal
        └── squamous
```

⚠️ The dataset is **not included in this repository** due to size limitations.

---

## Model Architecture

The Convolutional Neural Network consists of the following layers:

- **Convolution Layers** – Extract spatial features from CT scan images  
- **MaxPooling Layers** – Reduce spatial dimensions and retain important features  
- **Flatten Layer** – Converts feature maps into a 1D vector  
- **Dense Layers** – Perform classification based on extracted features  
- **Softmax Output Layer** – Produces probability scores for the four classes  

---

## Model Performance

After training the CNN model:

| Metric | Value |
|------|------|
| Training Accuracy | ~96% |
| Validation Accuracy | ~94% |
| Test Accuracy | ~93% |

These results show that the model performs well in classifying lung CT scan images.

---

## Streamlit Web Application

A **Streamlit-based web interface** was developed to make the model easy to use.

### Features

- Upload CT scan image
- Model predicts cancer type
- Displays prediction confidence
- Visualization of prediction probabilities

### Example Workflow

1. Upload CT scan image
2. Model processes the image
3. Prediction result is displayed

---

## Project Structure

```
lung-cancer-cnn/
│
├── notebooks/
│   └── lung_cancer_training.ipynb
│
├── models/
│   └── lung_cancer_cnn.h5
│
├── data/
│   └── Lung Cancer Detection Dataset
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Raghavj1401/lung-cancer-cnn.git
cd lung-cancer-cnn
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Streamlit Application

```bash
streamlit run app.py
```

Then open the provided **local URL** in your browser.

---

## Technologies Used

- Python
- TensorFlow / Keras
- NumPy
- Matplotlib
- Streamlit

---

## Future Improvements

- Use a larger dataset
- Apply transfer learning (ResNet / EfficientNet)
- Improve model generalization
- Deploy the application online

---

## Author

**Raghav Joshi**  
B.Tech Electrical Engineering  

Email: raghavjoshi200314@gmail.com  

---

## License

This project is developed for **educational and research purposes**.
