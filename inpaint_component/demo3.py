import gradio as gr
import time
from PIL import Image
import numpy as np

t = [[[1,2,3],[2,3,4]],
     [[4,5,6], [5,6,7]]]
mask = [[True, False],
        [True, False]]
t, mask = np.array(t), np.array(mask)

t[mask] = t[mask, ::-1]
t


def rgb_to_bgr(paint) :
    image, mask = paint['image'], paint['mask'].convert('L')
    image, mask = np.array(image), np.array(mask)

    mask_bool = np.where(mask > 128, True, False)
    image[mask_bool] = image[mask_bool, ::-1]
    return Image.fromarray(image)

with gr.Blocks() as demo:
    with gr.Row():
        input_img = gr.Image(label='Input', type='pil', image_mode='RGB', source='upload', tool='sketch')

        output_img = gr.Image(label='Output', type='pil', image_mode='RGB')
    
    with gr.Row() :
        btn = gr.Button("Run", variant="primary")

    btn.click(fn=rgb_to_bgr, inputs=[input_img], outputs=[output_img])

demo.launch()