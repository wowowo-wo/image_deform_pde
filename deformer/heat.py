import cv2
import numpy as np
from PIL import Image

def heat_deform(img_path,output_path="heat_result.gif",
                num_iter=240, skip_step=1, weight=0.2,
                noise_freq=None, noise_strength=0.0) :
    
    img = cv2.imread(img_path)

    if img is None:
        raise FileNotFoundError("File is not found")
    
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB).astype(np.float32)

    curr = img.copy()
    frames = []

    for t in range(num_iter):
        next_img = np.zeros_like(curr)
        for c in range(3):
            u = curr[:,:,c]
            laplacian = (np.roll(u, 1, axis=0) + np.roll(u, -1, axis=0) +
                         np.roll(u, 1, axis=1) + np.roll(u, -1, axis=1) - 4 * u)
            next_img[:, :, c] = curr[:, :, c] + weight * laplacian

        if noise_freq is not None:
            if np.random.rand() < 1 / noise_freq:
                noise = np.random.normal(0, noise_strength, curr.shape).astype(np.float32)
                next_img += noise

        if t % skip_step == 0:
            frame = np.clip(curr, 0, 255).astype(np.uint8)
            frames.append(Image.fromarray(frame))
        
        curr = next_img.copy()

    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=100, loop=0)
    print(f"saved in {output_path}")