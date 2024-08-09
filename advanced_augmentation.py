import Augmentor

image_folder_path = r'images\initial'

pipeline = Augmentor.Pipeline(image_folder_path, output_directory=r'..\..\images\post_augmentation')

pipeline.rotate(probability=0.5, max_left_rotation=5, max_right_rotation=5)
pipeline.flip_left_right(probability=0.3)
pipeline.random_distortion(probability=0.3, grid_width=3, grid_height=3, magnitude=5)

number_of_augmented_images = 100 
pipeline.sample(number_of_augmented_images)
