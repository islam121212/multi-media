from flask import Flask, render_template, jsonify, request, send_from_directory
import pyttsx3
from werkzeug.utils import secure_filename
import os
import threading
import logging
import datetime

app = Flask(__name__)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

UPLOAD_FOLDER = r'C:\Users\eslam\Desktop\muti-media_project\uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def convert_text_to_audio(text, audio_path):
    try:
        engine.save_to_file(text, audio_path)
        engine.runAndWait()
        engine.stop()
        logging.info(f"Audio file created at {audio_path}")
    except Exception as e:
        logging.error(f"Error during text-to-speech conversion: {e}")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/convert_file_to_audio', methods=['POST'])
def convert_file_to_audio():
    if 'file' not in request.files:
        logging.error("No file part in the request.")
        return jsonify({"message": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        logging.error("No file selected.")
        return jsonify({"message": "No selected file"}), 400

    try:
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        file.save(file_path)
        logging.info(f"File saved at {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        logging.info("File content read successfully.")

        audio_filename = f"{filename.rsplit('.', 1)[0]}.mp3"
        audio_path = os.path.join(UPLOAD_FOLDER, audio_filename)

        os.makedirs(os.path.dirname(audio_path), exist_ok=True)

        thread = threading.Thread(target=convert_text_to_audio, args=(content, audio_path))
        thread.start()

        return jsonify({"message": "Audio conversion started.", "audio_file": audio_filename}), 200

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({"message": str(e)}), 500

@app.route('/download/<filename>')
def download_file(filename):
    if not filename.endswith('.mp3'):
        return jsonify({"message": "Invalid file format"}), 400
    
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
