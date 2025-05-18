import streamlit as st
from deformer import wave_deform, heat_deform
import os

st.title("image_deform_pde")

mode = st.selectbox("Choose mode", ["wave", "heat"])

if mode == "wave":
    st.header("Wave Deformation")
    img1 = st.file_uploader("Upload Image 1", type=["jpg","jpeg","png","webp"])
    img2 = st.file_uploader("Upload Image 2", type=["jpg","jpeg","png","webp"])
    
    num_iter = st.slider("Number of iterations", 10, 1000, 240)
    skip_step = st.slider("Skip step", 1, 20, 1)
    weight = st.slider("Wave strength (weight)", 0.0, 0.25, 0.1)
    noise_freq = st.slider("Noise frequency", value=0, step=1)
    noise_strength = st.slider("Noise strength", 0.0, 500.0, 0.0)
    
    if st.button("Run Wave Deformation") and img1 and img2:
        with open("tmp_img1.png", "wb") as f:
            f.write(img1.read())
        with open("tmp_img2.png", "wb") as f:
            f.write(img2.read())
        
        wave_deform(
            img1_path="tmp_img1.png",
            img2_path="tmp_img2.png",
            output_path="wave_result.gif",
            num_iter=num_iter,
            skip_step=skip_step,
            weight=weight,
            noise_freq=noise_freq if noise_freq > 0 else None,
            noise_strength=noise_strength,
        )
        st.image("wave_result.gif")

elif mode == "heat":
    st.header("Heat Deformation")
    img = st.file_uploader("Upload Image", type=["jpg","jpeg","png","webp"])
    
    num_iter = st.slider("Number of iterations", 10, 1000, 240)
    skip_step = st.slider("Skip step", 1, 20, 1)
    weight = st.slider("Blur strength (weight)", 0.0, 0.25, 0.1)
    noise_freq = st.slider("Noise frequency", value=0, step=1)
    noise_strength = st.slider("Noise strength", 0.0, 500.0, 0.0)
    
    if st.button("Run Heat Deformation") and img:
        with open("tmp_input.png", "wb") as f:
            f.write(img.read())

        heat_deform(
            img_path="tmp_input.png",
            output_path="heat_result.gif",
            num_iter=num_iter,
            skip_step=skip_step,
            weight=weight,
            noise_freq=noise_freq if noise_freq > 0 else None,
            noise_strength=noise_strength,
        )
        st.image("heat_result.gif")
