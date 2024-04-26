from flask import Flask, render_template, request
import pyttsx3
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fitness_booking')
def fitness_booking():
    return render_template('fitness_booking.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No selected file'
    
    if file:
        # Save the uploaded file
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)
        
        # Initialize text-to-speech engine
        engine = pyttsx3.init()
        
        # Read the file
        with open(filepath, 'r') as f:
            text = f.read()
        
        engine.say(text)
        engine.runAndWait()
        
        return 'File uploaded and read successfully'

if __name__ == '__main__':
    app.run(debug=True)