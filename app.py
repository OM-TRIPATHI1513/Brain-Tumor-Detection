import gradio as gr
import numpy as np
from PIL import Image
import tensorflow as tf
import datetime
import json
import os

# Load your trained model
model = tf.keras.models.load_model('my_model.keras')
print("✅ Model loaded successfully.")

# Create history.json if not exists
if not os.path.exists("history.json"):
    with open("history.json", "w") as f:
        f.write("")

def predict(image: Image.Image):
    # Preprocess
    img = image.resize((64, 64))
    img = np.array(img).astype('float32') / 255.0
    input_img = np.expand_dims(img, axis=0)

    # Prediction
    predictions = model.predict(input_img)
    tumor_probability = predictions[0][1] * 100
    binary_result = "Yes" if tumor_probability >= 30 else "No"

    # Save result
    record = {
        "timestamp": datetime.datetime.now().isoformat(),
        "prediction": binary_result,
        "probability": f"{tumor_probability:.2f}%"
    }
    with open("history.json", "a") as f:
        f.write(json.dumps(record) + "\n")

    return f"Tumor Probability: {tumor_probability:.2f}%", f"Tumor Presence: {binary_result}"

# Gradio UI
demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=["text", "text"],
    title="🧠 Brain Tumor Detection",
    description="Upload a brain MRI image to detect tumor presence. Trained using CNN."
)

if __name__ == "__main__":
    demo.launch()
