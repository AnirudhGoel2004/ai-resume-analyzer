def score_resume(resume_text, job_keywords):
    # Match skills between resume and job description
    resume_skills = set(resume_text['skills'])
    job_skills = set(job_keywords)
    
    matched_skills = resume_skills.intersection(job_skills)
    missing_skills = job_skills.difference(resume_skills)
    
    # Calculate a score based on matched skills
    score = len(matched_skills) / len(job_skills) * 100
    feedback = {
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills)
    }
    
    return score, feedback
