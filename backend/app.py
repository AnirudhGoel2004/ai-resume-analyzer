from flask import Flask, request, jsonify
from resume_parser import parse_resume
from job_description_parser import parse_job_description
from models import score_resume
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Welcome to the AI-powered Resume Analyzer API"

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/upload-resume', methods=['POST'])
def upload_resume():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    text = parse_resume(file)
    return jsonify({'resume_text': text})

@app.route('/upload-job-description', methods=['POST'])
def upload_job_description():
    data = request.get_json()
    job_description = data['job_description']
    parsed_job = parse_job_description(job_description)
    return jsonify({'job_keywords': parsed_job})

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    data = request.get_json()
    resume_text = data['resume_text']
    job_description = data['job_keywords']
    score, feedback = score_resume(resume_text, job_description)
    return jsonify({'score': score, 'feedback': feedback})

if __name__ == '__main__':
    app.run(debug=True)
