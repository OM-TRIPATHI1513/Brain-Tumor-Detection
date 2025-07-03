# 🧠 Brain Tumor Detection Using CNN + Gradio

This project implements a deep learning-based web application to detect brain tumors from MRI images. It uses a Convolutional Neural Network (CNN) model and provides an interactive interface using Gradio. The app is deployed on Hugging Face Spaces for free and easy public access.

---

## 📑 Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Code Overview](#code-overview)
- [Model Details](#model-details)
- [Deployment (Hugging Face)](#deployment-hugging-face)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)

---

## ✅ Requirements

Make sure the following Python libraries are installed:

- Python 3.x
- TensorFlow / Keras
- NumPy
- OpenCV
- Pillow
- Gradio

You can install everything with:

```bash
pip install -r requirements.txt
```

---

## 📦 Installation

Clone the project:

```bash
git clone https://huggingface.co/spaces/Pt-OM-TRIPATHI/Brain-Tumor-Detection
cd Brain-Tumor-Detection
```

Place your trained model file (`my_model.keras`) in the root directory if not already included.

---

## 🚀 Usage

Run the app locally with:

```bash
python app.py
```

Then open the link in your browser:

```
http://127.0.0.1:7860
```

---

## 🗂 Project Structure

```
Brain-Tumor-Detection/
│
├── app.py                  # Gradio web app for inference
├── my_model.keras          # Trained CNN model (64x64 input)
├── requirements.txt        # All Python dependencies
├── uploads/                # Temp folder for uploaded images
├── history.json            # Stores prediction logs
├── static/style.css        # (Optional) Flask styling file
├── templates/index.html    # (Optional) HTML template (if Flask used)
└── README.md               # You're reading it!
```

---

## 🧠 Code Overview

### app.py

- Loads CNN model (`my_model.keras`)
- Accepts image uploads via Gradio
- Preprocesses images: resize to 64x64, normalize
- Predicts tumor presence probability
- Displays result and prediction percentage
- Optionally logs results to `history.json`

### Sample Output:

```
Tumor Probability: 94.27%
Prediction: Tumor Present
```

---

## 📊 Model Details

| Attribute           | Value                  |
|---------------------|------------------------|
| Model Type          | CNN                    |
| Input Size          | 64x64 RGB              |
| Layers              | Conv → MaxPool → Dense |
| Activation          | ReLU / Softmax         |
| Accuracy (Test Set) | ~96%                   |
| Output              | Tumor / No Tumor       |

Model trained using categorical crossentropy loss and Adam optimizer.

---

## 🌐 Deployment (Hugging Face)

App is live at:

🔗 **[https://huggingface.co/spaces/Pt-OM-TRIPATHI/Brain-Tumor-Detection](https://huggingface.co/spaces/Pt-OM-TRIPATHI/Brain-Tumor-Detection)**

![image](https://github.com/user-attachments/assets/7328336f-250c-4011-906c-4299168861d4)

Steps to Deploy Your Own:


1. Create a new **Space** on [Hugging Face Spaces](https://huggingface.co/spaces)
2. Set the **type** to `Gradio`
3. Push your code:

```bash
git add .
git commit -m "Deploy Brain Tumor Detection"
git push
```

That's it! Hugging Face handles the build and deploy automatically.

---

## 🔮 Future Enhancements

- ✅ Grad-CAM visualization for model transparency
- ✅ Custom decision threshold slider
- ✅ Patient history tracking system
- ✅ Docker container for easy setup
- ✅ Training UI for model updates (future)

---

## 🤝 Contributing

Want to improve this project?

- Fork the repo
- Create a feature branch
- Submit a pull request

---

## 📝 License

This project is licensed under the **MIT License**.

---

## 👨‍⚕️ Made by

**Om Tripathi**  
🔗 [Profile](https://huggingface.co/Pt-OM-TRIPATHI)

> Empowering early diagnosis using AI and accessible web tools.



