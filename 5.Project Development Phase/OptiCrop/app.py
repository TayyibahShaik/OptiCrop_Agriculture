from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load model and scaler
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)
except FileNotFoundError:
    model = None
    scaler = None
    print("Warning: model.pkl or scaler.pkl not found. Please run model_training.py first.")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/findyourcrop', methods=['GET', 'POST'])
def findyourcrop():
    if request.method == 'POST':
        # Retrieve data from form
        try:
            N = float(request.form.get('N'))
            P = float(request.form.get('P'))
            K = float(request.form.get('K'))
            temperature = float(request.form.get('temperature'))
            humidity = float(request.form.get('humidity'))
            ph = float(request.form.get('ph'))
            rainfall = float(request.form.get('rainfall'))
            
            # Preprocess the data as done during training (log transform on Potassium)
            K = np.log1p(K)
            
            # Prepare input features
            input_features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            
            # Scale features
            if scaler and model:
                input_scaled = scaler.transform(input_features)
                prediction = model.predict(input_scaled)[0]
                return render_template('findyourcrop.html', prediction_text=f'The most suitable crop for your conditions is: {prediction.capitalize()}')
            else:
                return render_template('findyourcrop.html', prediction_text='Error: Model is not trained yet.')
                
        except ValueError:
            return render_template('findyourcrop.html', prediction_text='Error: Please enter valid numerical values.')
            
    return render_template('findyourcrop.html')

if __name__ == '__main__':
    app.run(debug=True)
