import spacy

nlp = spacy.load("en_core_web_sm")

def parse_job_description(text):
    doc = nlp(text)
    
    # Extract keywords, skills, and other important sections
    job_keywords = [ent.text for ent in doc.ents if ent.label_ == 'SKILL']
    
    return job_keywords
