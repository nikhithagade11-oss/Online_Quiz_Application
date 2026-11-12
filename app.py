from flask import Flask, render_template, request, session
import sqlite3
from database import (
    create_database,
    insert_questions,
    get_questions,
    get_random_questions,
    get_questions_by_ids,
    get_results
)


app = Flask(__name__)
app.secret_key = "quiz-secret-key"

# Initialize database
create_database()
insert_questions()


@app.route("/")
def home():
    return "Welcome to Online Quiz Application!"
@app.route("/quiz")
def quiz():
    questions = get_random_questions()

    session["question_ids"] = [
        question["id"] for question in questions
    ]

    return render_template("quiz.html", questions=questions)
@app.route("/result", methods=["POST"])
def result():
    question_ids = session.pop("question_ids", [])
    questions = get_questions_by_ids(question_ids)

    score = 0
    review = []

    for i, question in enumerate(questions):
        selected = request.form.get(str(i))

        is_correct = selected == question["answer"]

        if is_correct:
            score += 1

        review.append({
            "question": question["question"],
            "selected": selected,
            "answer": question["answer"],
            "is_correct": is_correct
        })

    connection = sqlite3.connect("quiz.db")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO results (score, total)
        VALUES (?, ?)
    """, (score, len(questions)))

    connection.commit()
    connection.close()

    return render_template(
        "result.html",
        score=score,
        total=len(questions),
        review=review
    )




@app.route("/history")
def history():
    results = get_results()
    return render_template("history.html", results=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
