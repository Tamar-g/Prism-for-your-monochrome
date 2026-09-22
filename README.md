# Prism for your monochrome - AI Image Colorization System

An AI-based image colorization system that transforms monochrome images into color images using **Deep Learning, GANs, and U-Net architectures**.

The project combines a **PyTorch-based Deep Learning backend**, image-processing pipelines, a REST API, and a React frontend to create an end-to-end image colorization application.

https://github.com/user-attachments/assets/f0916861-7963-4b5a-bfc5-1addac3da46e

## Overview

The system receives a grayscale image and generates a colorized version using a trained neural-network pipeline.

The core colorization model combines **U-Net-based image processing with Generative Adversarial Network (GAN) concepts**, enabling the system to learn visual representations and generate plausible color information.

The project covers the complete workflow from image input and preprocessing through model inference and final visualization.

## System Architecture

```text
                 ┌─────────────────┐
                 │   React Client  │
                 │                 │
                 │  Image Upload   │
                 │  Visualization  │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │    REST API     │
                 │                 │
                 │ Request / Image │
                 │    Handling     │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ PyTorch Backend │
                 │                 │
                 │   Preprocess    │
                 │       ↓         │
                 │    U-Net / GAN  │
                 │       ↓         │
                 │    Inference    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Colorized Image │
                 │                 │
                 │ Post-processing │
                 │   & Output      │
                 └─────────────────┘
```

## Key Features

* Automated grayscale-to-color image generation
* Deep Learning-based image processing
* GAN-based architecture
* U-Net image-to-image architecture
* PyTorch model implementation
* Image preprocessing and post-processing
* REST API integration
* React-based user interface
* End-to-end inference pipeline

## Deep Learning Pipeline

The colorization workflow includes several stages:

### 1. Image Input

A monochrome image is provided as the input to the system.

### 2. Preprocessing

The input image is prepared for neural-network inference using image-processing operations and numerical transformations.

### 3. Model Inference

The processed image is passed through the Deep Learning pipeline based on **U-Net and GAN architectures**.

The model learns relationships between image structure and color information and generates a colorized representation.

### 4. Post-processing

The generated output is processed and converted into a viewable color image.

### 5. Application Output

The final result is returned through the backend and displayed through the React interface.

## Technologies

| Category             | Technologies |
| -------------------- | ------------ |
| Programming          | Python       |
| Deep Learning        | PyTorch      |
| Neural Networks      | GAN, U-Net   |
| Numerical Processing | NumPy        |
| Image Processing     | Pillow       |
| Backend              | REST API     |
| Frontend             | React        |
| Database             | SQL          |
| Version Control      | Git          |

## Engineering & AI Focus

The project provides hands-on experience with:

* Deep Learning systems
* Neural-network architectures
* Image-to-image transformation
* GAN-based model development
* U-Net architectures
* Model inference pipelines
* Image preprocessing and post-processing
* Backend/frontend integration
* REST API communication
* Analysis of AI-generated outputs

## Project

**GitHub:** [Tamar-g/Prism-for-your-monochrome](https://github.com/Tamar-g/Prism-for-your-monochrome)
