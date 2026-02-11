import cv2
import os
import glob
import numpy as np

INPUT_DIR = "input_images"
OUTPUT_DIR = "output_images"

def process_images():
    # Check if output folder is existing in repo
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Code to check all images found in input folder
    image_files = glob.glob(os.path.join(INPUT_DIR, "*"))
    print(f"Found {len(image_files)} images...")

    for file_path in image_files:
        img = cv2.imread(file_path)
        if img is None:
            continue
        
        filename = os.path.basename(file_path)
        name, ext = os.path.splitext(filename)

        # Technique 1. Thermal Vision
        thermal = cv2.applyColorMap(img, cv2.COLORMAP_JET)
        cv2.imwrite(os.path.join(OUTPUT_DIR, f"thermal_{filename}"), thermal)

        # Technique 2. Directional Motion Blur
        kernel_size = 15
        kernel = np.zeros((kernel_size, kernel_size))
        kernel[int((kernel_size-1)/2), :] = np.ones(kernel_size) / kernel_size
        motion = cv2.filter2D(img, -1, kernel)
        cv2.imwrite(os.path.join(OUTPUT_DIR, f"motion_{filename}"), motion)

        # Technique 3. Mirror Flip
        mirror = cv2.flip(img, 1)
        cv2.imwrite(os.path.join(OUTPUT_DIR, f"mirror_{filename}"), mirror)

        # Technique 4. Channel Swap (BGR -> RGB)
        swap = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imwrite(os.path.join(OUTPUT_DIR, f"swap_{filename}"), swap)

        # Technique 5. Solarize (Invert only pixels above 128)
        solar = img.copy()
        mask = solar > 128
        solar[mask] = 255 - solar[mask]
        cv2.imwrite(os.path.join(OUTPUT_DIR, f"solar_{filename}"), solar)

        # Technique 6. Rotate 90 Degrees Clockwise
        rotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(os.path.join(OUTPUT_DIR, f"rotate_{filename}"), rotate)

        print(f"Processed: {filename}")

if __name__ == "__main__":
    process_images()
