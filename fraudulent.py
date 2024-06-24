import joblib
import numpy as np
import pandas as pd
import string
from flask import Flask, request, jsonify, render_template
from gensim.models import FastText
import nltk
from nltk.corpus import stopwords
import os

#Download necessary NLTK resources
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

#Initialize Flask application
app = Flask(__name__)


#Load the pre-trained FastText model and the best RF model
ft_model = joblib.load('fasttext_model_fraudulent.bin')
best_rf_model = joblib.load('RF_model_alpha.pkl')

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return ' '.join(tokens)

# Function to vectorize text using FastText
def vectorize_text(text, model):
    words = text.split()
    word_vectors = [model.wv[word] for word in words if word in model.wv]
    if word_vectors:
        text_vector = np.mean(word_vectors, axis=0)
    else:
        text_vector = np.zeros(model.vector_size)
    return text_vector



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'description' in request.form:
        description = request.form['description']
        #Preprocess the text
        preprocessed_text = preprocess_text(description)
        #Vectorize the text
        vectorized_text = vectorize_text(preprocessed_text, ft_model).reshape(1, -1)
        #Make prediction
        prediction = best_rf_model.predict(vectorized_text)
        #Return the prediction
        result = 'Fraudulent' if prediction[0] == 1 else 'Not Fraudulent'
        return render_template('index.html', prediction_text=f'Prediction: {result}')
    else:
        return render_template('index.html', prediction_text='No description provided')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)