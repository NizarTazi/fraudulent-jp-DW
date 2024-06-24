# Fraud Detection API

This project provides a Flask-based API for predicting whether job descriptions are fraudulent using a pre-trained FastText model and a Random Forest classifier.

## Table of Contents
- [Requirements](#requirements)
- [Setup](#setup)
- [Running the Application](#running-the-application)
- [Usage](#usage)

## Requirements
- [Docker](https://www.docker.com/products/docker-desktop)

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


## Docker
1. Open Docker Desktop: Ensure Docker Desktop is running.
2. Open Terminal: Open Git Bash, Command Prompt, or PowerShell.
3. Navigate to Project Directory
   

### 3. Build the Docker image
To build the Docker image, run the following command in the project directory:
```sh
docker build -t fraud-detection-api .
```

## Running the application
### 4. Run the Docker container
To run the Docker container, use the following command:
```sh
docker run -p 5000:5000 fraud-detection-api
```

### 5. Browse to the Application

Open your web browser and navigate to: http://127.0.0.1:5000/

## Usage

    You will be prompted with a text box and a predict button.
    Type job postings into the text box and click the predict button.
    The algorithm will predict if the job posting is fraudulent or not fraudulent.


