import torch
import gradio as gr
from diffusers import StableDiffusionPipeline
from PIL import Image


MODEL_ID = "runwayml/stable-diffusion-v1-5"

pipe = StableDiffusionPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float32
)


pipe = pipe.to("cpu")


# Image Generation Function

def generate_image(prompt):
    if prompt is None or prompt.strip() == "":
        return None

    image = pipe(prompt).images[0]

    return image

# Gradio Interface

with gr.Blocks(title="Text to Image Generator") as demo:
    gr.Markdown(
         """
        #  Text-to-Image Generator
        **Created by Saravanan R**

        A free Generative AI project that converts text prompts into images  
        using **Stable Diffusion**, **PyTorch**, **Diffusers**, and **Gradio**.
        """
    )

    prompt_input = gr.Textbox(
        label="Enter your prompt",
        lines=2
    )

    generate_btn = gr.Button("Generate Image")

    output_image = gr.Image(label="Generated Image")

    generate_btn.click(
        fn=generate_image,
        inputs=prompt_input,
        outputs=output_image
    )

    gr.Markdown(
        """
        ---
        **Project by Saravanan R**  
        Built for learning, experimentation, and portfolio showcase.
        """
    )

demo.launch()
