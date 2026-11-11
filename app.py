
from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "1. Which language is used for web development?",
        "options": ["Python", "HTML", "C", "All of these"],
        "answer": "All of these"
    },
    {
        "question": "2. Which keyword is used to define a function in Python?",
        "options": ["function", "def", "fun", "define"],
        "answer": "def"
    },
    {
        "question": "3. What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Control Processing User"
        ],
        "answer": "Central Processing Unit"
    },
    {
        "question": "4. Which data type stores True or False?",
        "options": ["int", "float", "bool", "str"],
        "answer": "bool"
    },
    {
        "question": "5. Which company developed Python?",
        "options": ["Microsoft", "Google", "Guido van Rossum", "Apple"],
        "answer": "Guido van Rossum"
    }
]

@app.route("/")
def home():
    return "Welcome to Online Quiz Application!"

@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=questions)

@app.route("/result", methods=["POST"])
def result():
    score = 0

    for i, question in enumerate(questions):
        selected = request.form.get(str(i))

        if selected == question["answer"]:
            score += 1

    return render_template(
        "result.html",
        score=score,
        total=len(questions)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
