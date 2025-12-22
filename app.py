import os

os.environ["HF_HOME"] = "/tmp"
os.environ["TRANSFORMERS_CACHE"] = "/tmp"

import gradio as gr
from diffusers import StableDiffusionPipeline

MODEL_ID = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID,
    safety_checker=None,
    low_cpu_mem_usage=True
)

pipe.enable_attention_slicing()
pipe = pipe.to("cpu")


def generate_image(prompt):
    if not prompt or prompt.strip() == "":
        return None, ""

    image = pipe(prompt).images[0]       

    return image

iface = gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(label="Enter prompt"),
    outputs=[
        gr.Image(type="pil", label="Generated Image")
        
    ],
    title="Text-to-Image Generator"
)

iface.launch()