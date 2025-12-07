from flask import Flask, render_template, request
from extractor import extract_resume_skills

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    skills = None
    error = None

    if request.method == "POST":
        if "resume" not in request.files:
            error = "Please upload a file."
        else:
            resume = request.files["resume"]
            if resume.filename == "":
                error = "No file selected."
            else:
                try:
                    skills = extract_resume_skills(resume)
                except Exception as e:
                    error = str(e)

    return render_template("index.html", skills=skills, error=error)

if __name__ == "__main__":
    app.run(debug=True)