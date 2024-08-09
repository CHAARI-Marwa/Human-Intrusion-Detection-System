import os
from PIL import Image, ImageEnhance
import random

def augment_images(input_folder, output_folder, target_count=50):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        img = Image.open(os.path.join(input_folder, filename))

        if img.mode == 'RGBA':
            img = img.convert('RGB')

        for i in range(target_count):
            angle = random.randint(-45, 45)
            rotated_img = img.rotate(angle)

            enhancer = ImageEnhance.Contrast(rotated_img)
            factor = random.uniform(0.5, 2.0)
            zoomed_img = enhancer.enhance(factor)

            base_filename = os.path.splitext(filename)[0]
            augmented_filename = f'augmented_{i}_{base_filename}.jpg'

            zoomed_img.save(os.path.join(output_folder, augmented_filename))

input_folder_path = r'images\initial'
output_folder_path = r'images\post_augmentation'
augment_images(input_folder_path, output_folder_path)
