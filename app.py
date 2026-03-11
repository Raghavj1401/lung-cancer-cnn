import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Lung Cancer Detection", layout="wide")

st.title("Lung Cancer Detection using CNN")

st.write("Upload a CT scan image to detect lung cancer type.")

# Load trained model
model = tf.keras.models.load_model("models/lung_cancer_cnn.h5")

# Class labels (must match dataset order)
class_names = ['adenocarcinoma', 'large_cell', 'normal', 'squamous']

# Upload image
uploaded_file = st.file_uploader("Upload CT Scan", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    # Open image
    image = Image.open(uploaded_file).convert("RGB")

    # Show uploaded image
    st.image(image, caption="Uploaded CT Scan", width=400)

    # Resize image
    img = image.resize((224, 224))

    # Convert to numpy
    img_array = np.array(img)

    # Normalize image
    img_array = img_array.astype("float32") / 255.0

    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)

    # Model prediction
    prediction = model.predict(img_array, verbose=0)

    score = prediction[0]

    predicted_class = class_names[np.argmax(score)]
    confidence = np.max(score)

    st.subheader("Prediction Result")

    st.write(f"Prediction: **{predicted_class}**")
    st.write(f"Confidence: **{confidence*100:.2f}%**")

    # Plot prediction probabilities
    fig, ax = plt.subplots()

    ax.bar(class_names, score)

    ax.set_ylabel("Probability")
    ax.set_title("Prediction Confidence")

    st.pyplot(fig)

    st.write(score)