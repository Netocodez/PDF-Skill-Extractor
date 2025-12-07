import docx.document
import spacy
import PyPDF2
import docx
import re

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

TECH_SKILLS = {
    "python", "java", "javascript", "react", "node.js", "html", "css",
    "docker", "kubernetes", "aws", "azure", "git", "sql", "mongodb",
    "c++", "c#", "linux", "flask", "django", "tensorflow", "pytorch"
}

doc = docx.Document("ONYENETO.docx")
text = "\n".join([p.text for p in doc.paragraphs])

docs = nlp(text.lower())

tokens = [token.text for token in docs if not token.is_stop and not token.is_punct]

skills = set()
for token in tokens:
    if token in TECH_SKILLS:
        skills.add(token)
print(skills)