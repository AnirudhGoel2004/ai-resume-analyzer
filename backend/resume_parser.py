import spacy
from pdfminer.high_level import extract_text

nlp = spacy.load("en_core_web_sm")

def parse_resume(file):
    # Extract text from the uploaded PDF or DOCX
    text = extract_text(file)  # Using pdfminer for PDF extraction
    doc = nlp(text)
    
    # Extract relevant sections (skills, education, etc.)
    skills = [ent.text for ent in doc.ents if ent.label_ == 'SKILL']
    experience = [ent.text for ent in doc.ents if ent.label_ == 'WORK_OF_ART']  # Modify this based on entities
    education = [ent.text for ent in doc.ents if ent.label_ == 'EDUCATION']
    
    parsed_resume = {
        "skills": skills,
        "experience": experience,
        "education": education,
    }
    
    return parsed_resume
