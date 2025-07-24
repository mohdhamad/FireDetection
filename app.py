from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# Load trained model
model = joblib.load('fire_model.pkl')

@app.route('/')
def home():
    return render_template('welcome.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/stations')
def stations():
    return render_template('stations.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(request.form[f'feature{i+1}']) for i in range(12)]
        final_features = np.array([data])
        prediction = model.predict(final_features)
        result = "🔥 High chance of forest fire!" if prediction[0] == 1 else "✅ Low chance of forest fire."
        return render_template('result.html', prediction=result)
    except Exception as e:
        return str(e)

@app.route('/detect_image', methods=['POST'])
def detect_image():
    file = request.files['image']
    if file.filename == '':
        return "No file selected!"
    filename = file.filename
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Basic keyword-based detection
    lower_name = filename.lower()
    if 'fire' in lower_name:
        result = "🔥 Fire Detected in Image!"
    elif 'smoke' in lower_name:
        result = "💨 Smoke Detected in Image!"
    else:
        result = "✅ No Fire Detected in Image."

    return render_template('result.html', prediction=result, image_url=file_path)

if __name__ == '__main__':
    app.run(debug=True)
