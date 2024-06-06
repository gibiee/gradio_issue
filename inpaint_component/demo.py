import gradio as gr
import time
from PIL import Image

def rgb_to_bgr(paint) :
    print(paint)
    print(type(paint))
    return 


with gr.Blocks() as demo:
    with gr.Row():
        input_img = gr.ImageEditor(label='Input', type='pil', image_mode='RGBA', sources=['upload'], layers=False,
                                   brush=gr.Brush(colors=["#000000AA"], color_mode="fixed"))

        output_img = gr.Image(label='Output', type='pil', image_mode='RGB')
    
    with gr.Row() :
        btn = gr.Button("Run", variant="primary")

    btn.click(fn=rgb_to_bgr, inputs=[input_img], outputs=[output_img])

demo.launch()