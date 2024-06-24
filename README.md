# Fraud Detection API

This project provides a Flask-based API for predicting whether job descriptions are fraudulent using a pre-trained FastText model and a Random Forest classifier.

## Table of Contents
- [Requirements](#requirements)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [Usage](#usage)

## Requirements
- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) (Anaconda or Miniconda) (optional)
- Python 3.8.5

## Setup

### 1. Clone the Repository
First, clone the repository to your local machine:

```sh
git clone https://github.com/yourusername/fraud-detection-api.git
cd fraud-detection-api
```

### 2. Download the Trained FastText Model

Download the trained FastText model from this link: [Google Drive Link](https://drive.google.com/file/d/1HNGmHp2_TllGtqR-f27QDWxhAV8qFBCd/view?usp=drive_link)

Add the downloaded file to the main repository directory.

### 3. Create a New Python Environment (Optional)

It is recommended to create a new Conda environment. Please note that the used Python version is 3.8.5. Some packages could be deprecated in newer versions of Python.
```sh
conda create --name fraud-detection-env python=3.8.5
conda activate fraud-detection-env
```

### 4. Install Requirements
   
Install the required dependencies in the new environment:
```sh
python -m pip install -r requirements.txt
```

## running-the-application
### 5. Run the Application
   
Run the application using the following command:
```sh
python fraudulent.py
```

### 6. Browse to the Application

Open your web browser and navigate to: http://127.0.0.1:5000/

## Usage

    You will be prompted with a text box and a predict button.
    Type job postings into the text box and click the predict button.
    The algorithm will predict if the job posting is fraudulent or not fraudulent.


