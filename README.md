# Midterm-elecproj
Automated Image Processing is a Python-based image processing application that demonstrates the integration of computer vision techniques with DevOps automation. The system processes images using multiple image processing operations and ensures reliability through automated testing and Continuous Integration (CI) using GitHub Actions.

# Automated Image Processing

## Project Overview
Automated Image Processing is a Python-based image processing application that demonstrates the integration of computer vision techniques with DevOps automation. The system processes images using multiple image processing operations and ensures reliability through automated testing and Continuous Integration (CI) using GitHub Actions.

---

## Learning Objectives
- Apply image processing techniques using Python and OpenCV  
- Implement automated testing using PyTest  
- Configure and utilize a Continuous Integration (CI) pipeline with GitHub Actions  
- Understand DevOps workflows and automation concepts  

---

## Tools and Technologies
- Python 3  
- OpenCV (opencv-python)  
- NumPy  
- PyTest  
- Git and GitHub  
- GitHub Actions  

## Project Structure 
text
elec4-midterm\
│
\
├── .github
\
│   └── workflows
\
│       └── ci.yml                # GitHub Actions pipeline and Project Dependencies 
\
│ 
\
├── input_images                 # Drop images here (trigger CI) \
│   └── sample.jpg 
\
│ 
\
├── output_images/                # Processed images appear here \
│   └── sample_thermal.jpg  
│
\
├── processor.py                  # Image processing logic\
├── test_process.py               # Pytest validations\
├── requirements.txt              # Project Dependencies\
│       \
└── README.md

---

## Implemented Image Processing Features

### Thermal Vision (Heatmap)
Applies a JET colormap to visualize intensity variations within the image.

### Motion Blur (Directional)
Creates a horizontal motion blur effect using a custom kernel for dynamic visuals.

### Mirror Flip (Horizontal)
Flips images horizontally for mirror reflection effects.

### Channel Swap (BGR → RGB)
Converts OpenCV's BGR color space to standard RGB color format.

### Solarize
Inverts pixels with brightness above 128 for a solarization effect.

### Rotate 90° Clockwise
Rotates images 90 degrees in the clockwise direction.


## Author
- Clemente, Jose Fernando - Image Processing Lead 
- Dasico, Jerome - Security
- Moral, Justine - DevOps Engineer
- Ocillos, Amberdawn - Tester
- Quinto, Francis Kian - Documenter/ Presenter
