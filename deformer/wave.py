import cv2
import numpy as np
from PIL import Image

def wave_deform(img1_path, img2_path, output_path="wave_result.gif",
                num_iter=240, skip_step=1, weight=0.2,
                noise_freq=None, noise_strength=0.0) :
    
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    if img1 is None or img2 is None:
        raise FileNotFoundError("File is not found")
    
    h2,w2=img2.shape[:2]
    img1=cv2.resize(img1,(w2,h2),interpolation=cv2.INTER_LINEAR)

    img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB).astype(np.float32)
    img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB).astype(np.float32)

    prev = img1.copy()
    curr = img2.copy()
    frames = []

    for t in range(num_iter):
        next_img = np.zeros_like(curr)
        for c in range(3):
            u = curr[:,:,c]
            laplacian = (np.roll(u, 1, axis=0) + np.roll(u, -1, axis=0) +
                         np.roll(u, 1, axis=1) + np.roll(u, -1, axis=1) - 4 * u)
            next_img[:, :, c] = 2 * u - prev[:, :, c] + weight * laplacian

        if noise_freq is not None:
            if np.random.rand() < 1 / noise_freq:
                noise = np.random.normal(0, noise_strength, curr.shape).astype(np.float32)
                next_img += noise

        if t % skip_step == 0:
            frame = np.clip(curr, 0, 255).astype(np.uint8)
            frames.append(Image.fromarray(frame))
        
        prev, curr = curr, next_img.copy()

    frames[0].save(output_path, save_all=True, append_images=frames[1:], duration=100, loop=0)
    print(f"saved in {output_path}")