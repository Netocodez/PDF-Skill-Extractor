import spacy
import PyPDF2
import docx

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

TECH_SKILLS = {
    "python", "java", "javascript", "react", "node.js", "html", "css",
    "docker", "kubernetes", "aws", "azure", "git", "sql", "mongodb",
    "c++", "c#", "linux", "flask", "django", "tensorflow", "pytorch"
}

def extract_text_from_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def extract_text_from_docx(file):
    document = docx.Document(file)
    return "\n".join([p.text for p in document.paragraphs])

def clean_and_tokenize(text):
    doc = nlp(text.lower())
    return [token.text for token in doc if not token.is_stop and not token.is_punct]

def extract_tech_skills(text):
    tokens = clean_and_tokenize(text)
    return sorted({token for token in tokens if token in TECH_SKILLS})

def extract_resume_skills(file):
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(file)
    elif filename.endswith(".docx"):
        text = extract_text_from_docx(file)
    else:
        raise ValueError("Unsupported file format")

    return extract_tech_skills(text)