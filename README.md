<a name="readme-top"></a>

<div align="center">

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

</div>

<div align="center">
  <h1 style="font-size:50px">Human Intrusion Detection System</h1>
</div>

## Introduction
The Human Intrusion Detection System is a sophisticated project designed to secure specific areas by detecting human presence beyond authorized limits. Utilizing advanced computer vision and image processing techniques, this solution identifies individuals and triggers instant alerts in case of intrusion.

## Description
This project involves real-time face recognition using **`OpenCV`** and the **`face_recognition`** library. It captures video from a webcam, detects faces, and verifies if the detected face is authorized. If an unauthorized face is detected, an alert sound is played. The project also includes image augmentation functionality to enhance the dataset used for face recognition.

## Table of Contents
<details>
  <summary>Contents Overview</summary>
  <ol>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#programming-language-and-libraries">Programming Language and Libraries</a></li>
    <li><a href="#image-augmentation">Image Augmentation</a></li>
    <li><a href="#face-recognition-scenarios">Face Recognition Scenarios</a></li>
    <li><a href="#face-recognition-workflow">Face Recognition Workflow</a></li>
    <li><a href="#running-the-project">Running the Project</a></li>
  </ol>
</details>

## Installation
- **Prerequisites:**

This project was developed using **`Python 3.11.5`**. Please ensure that this version is installed on your system. If not, you can download it from the official [Python website](https://www.python.org/downloads/release/python-3115/).
- **Required Libraries:**

Install the necessary Python libraries by running the following command:

```bash
pip install opencv-python face_recognition Pillow Augmentor
```
- **Additional Requirements:**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-**OS Module**: This is a standard Python library, no installation required.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-**winsound Module**: This is available by default on Windows systems.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Programming Language and Libraries
- **Python:** The main programming language used for the project.
- **OpenCV:** Used for video capture and image processing.
- **face_recognition:** A Python library for detecting and encoding faces, built on dlib's state-of-the-art face recognition technology.
- **Pillow:** A library for image augmentation, including operations such as rotation and zoom.
- **Augmentor:** A library for advanced image augmentation techniques.
- **winsound:** Used for generating sound alerts in case of unauthorized access (**`Note`**: This is specific to Windows).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Image Augmentation

- **Basic Augmentation:**

A script is included (**`basic_augmentation.py`**) that performs basic image augmentation techniques, such as rotation and contrast enhancement.
 
- **Advanced Augmentation with Augmentor:**

For more complex augmentation, the project includes another script (**`advanced_augmentation.py`**) using the Augmentor library. This script allows for random distortions, rotations, and flipping of images, useful for creating a larger and more varied dataset for face recognition.

These scripts creates additional images based on the originals in the `images\initial` directory and saves them in the `images\post_augmentation` directory.

- **Note:** 
If the augmentation scripts are not optimally configured for your specific dataset, you can adjust the augmentation operations or parameters to better suit your needs. Additionally, modify the paths if you are working with more than one area.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Face Recognition Scenarios

- **Single Area:**

A script is included (**`face_recognition_single_area.py`**) that sets up the program to recognize and monitor one area. The program will alert if an unauthorized person is detected within the entire space.

- **Two Area:** 

For monitoring two areas, the project includes another script (**`face_recognition_two_areas.py`**). This configuration checks if individuals are within their respective designated areas and triggers an alert if any unauthorized persons are detected within the entire space.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Face Recognition Workflow
1. The face recognition program captures video from the webcam and detects faces in real-time.
2. It compares detected faces with known encodings (preloaded from images). The program can monitor one or two authorized areas and will indicate whether a face is "Authorized" or "Unauthorized."
3. If an unauthorized face is detected in any area, the program will trigger a sound alert.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Running the Project
1. **Clone this repository** to your local machine.
2. **Navigate to the project directory**.
3. **Create the `images/initial` directory**, and then **place the images of authorized individuals in this directory** for augmentation.
4. **Run the Image Augmentation Script**.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- **For `basic augmentation` :**
```bash
python basic_augmentation.py
````
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-**For `advanced augmentation` :**
```bash
python advanced_augmentation.py
```
5. **Run the Face Recognition Program**.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-**For `single area` :**
```bash
python face_recognition_single_area.py
````

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-**For `two areas` :**
```bash
python face_recognition_two_areas.py
```
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[forks-shield]: https://img.shields.io/github/forks/CHAARI-Marwa/Human-Intrusion-Detection-System.svg?style=for-the-badge
[forks-url]: https://github.com/CHAARI-Marwa/Human-Intrusion-Detection-System/network/members
[stars-shield]: https://img.shields.io/github/stars/CHAARI-Marwa/Human-Intrusion-Detection-System.svg?style=for-the-badge
[stars-url]: https://github.com/CHAARI-Marwa/Human-Intrusion-Detection-System/stargazers
[issues-shield]: https://img.shields.io/github/issues/CHAARI-Marwa/Human-Intrusion-Detection-System.svg?style=for-the-badge
[issues-url]: https://github.com/CHAARI-Marwa/Human-Intrusion-Detection-System/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/chaari-marwa/