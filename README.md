# 🎨 Text-to-Image Generator

## Live Link : https://huggingface.co/spaces/Saravana21/text-to-image-generator

**Created by Saravanan R**
## portfolio: https://agentic-learner-showcase.lovable.app

A free and open-source **Text-to-Image Generative AI application** that converts natural language prompts into images using **Stable Diffusion**.  
This project is built with **PyTorch**, **Diffusers**, **Transformers**, and **Gradio**, and can be run locally or deployed on Hugging Face Spaces.

---

## 🚀 Features

- Convert text prompts into images
- Uses **Stable Diffusion v1.5** (100% free and open-source)
- Simple and clean **Gradio UI**
- Runs on **CPU** (no GPU or API key required)
- Suitable for **learning, demos, and portfolio showcase**

---

## 🧠 Tech Stack

- Python
- PyTorch
- Diffusers
- Transformers
- Pillow
- Gradio

---

## 📁 Project Structure

text-to-image-generator/  
├── app.py  
├── requirements.txt  
└── README.md  

---

## ⚙️ Installation & Setup (Local)

### 1️⃣ Create a virtual environment


python -m venv sd_env
source sd_env/bin/activate   # Linux / macOS
sd_env\Scripts\activate      # Windows

2️⃣ Install dependencies
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install diffusers transformers accelerate pillow gradio

3️⃣ Run the application
python app.py

Open your browser and go to:

http://127.0.0.1:7860

✍️ Example Prompts
A cat eating pizza, realistic photography, natural lighting

An astronaut riding a green horse, realistic style

A peaceful Indian village in the morning sunlight

⏳ Performance Notes

The first run downloads the model (~4 GB)

On CPU, image generation may take 1–3 minutes

For faster testing, reduce inference steps in the code

🎯 Use Cases

Learning Generative AI concepts

AI / ML internship projects

Portfolio demonstration

Text-to-image experimentation

📌 Future Enhancements

Add negative prompt support

Add sliders for steps and guidance scale

Deploy on Hugging Face Spaces

Improve UI design and styling

👤 Author

Saravanan R
Aspiring Generative AI Engineer

Built as a hands-on Generative AI project for learning and showcasing skills.

📜 License

This project is open-source and intended for educational and personal use.
