
import sqlite3

DATABASE = "quiz.db"


# Create database and tables
def create_database():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    # Questions table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            options TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """)

    # Results table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


# Insert 20 questions into database
def insert_questions():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    questions = [
        ("Which language is used for web development?",
         "Python,HTML,C,All of these", "All of these"),

        ("Which keyword is used to define a function in Python?",
         "function,def,fun,define", "def"),

        ("What does CPU stand for?",
         "Central Processing Unit,Computer Personal Unit,Central Program Utility,Control Processing User",
         "Central Processing Unit"),

        ("Which data type stores True or False?",
         "int,float,bool,str", "bool"),

        ("Which company developed Python?",
         "Microsoft,Google,Guido van Rossum,Apple", "Guido van Rossum"),

        ("Which symbol is used for comments in Python?",
         "//,#,/*,<!--", "#"),

        ("Which function displays output in Python?",
         "input(),print(),display(),show()", "print()"),

        ("Which data type stores decimal values?",
         "int,float,str,bool", "float"),

        ("Which loop is used to iterate over a sequence?",
         "for,if,switch,break", "for"),

        ("Which keyword is used to create a class in Python?",
         "function,class,define,object", "class"),

        ("What is the extension of a Python file?",
         ".java,.py,.c,.html", ".py"),

        ("Which operator is used for exponentiation in Python?",
         "^,**,%,//", "**"),

        ("Which collection stores key-value pairs?",
         "List,Tuple,Dictionary,Set", "Dictionary"),

        ("Which keyword is used to handle exceptions?",
         "try,for,while,print", "try"),

        ("Which function returns the length of a list?",
         "size(),count(),len(),length()", "len()"),

        ("Which method adds an item to the end of a list?",
         "add(),append(),insertEnd(),push()", "append()"),

        ("Which value represents no value in Python?",
         "0,False,None,Empty", "None"),

        ("Which operator checks equality?",
         "=,==,!=,>=", "=="),

        ("Which keyword is used to import a module?",
         "include,using,import,library", "import"),

        ("Which function converts a value to an integer?",
         "str(),float(),int(),bool()", "int()")
    ]

    # Insert only questions that are not already present
    cursor.executemany("""
        INSERT INTO questions (question, options, answer)
        SELECT ?, ?, ?
        WHERE NOT EXISTS (
            SELECT 1 FROM questions WHERE question = ?
        )
    """, [q + (q[0],) for q in questions])

    connection.commit()
    connection.close()


# Retrieve all questions
def get_questions():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM questions")
    rows = cursor.fetchall()

    connection.close()

    questions = []

    for row in rows:
        questions.append({
            "id": row[0],
            "question": row[1],
            "options": row[2].split(","),
            "answer": row[3]
        })

    return questions
def get_random_questions():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM questions
        ORDER BY RANDOM()
        LIMIT 5
    """)

    rows = cursor.fetchall()
    connection.close()

    questions = []

    for row in rows:
        questions.append({
            "id": row[0],
            "question": row[1],
            "options": row[2].split(","),
            "answer": row[3]
        })

    return questions
def get_questions_by_ids(question_ids):
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    questions = []

    for question_id in question_ids:
        cursor.execute(
            "SELECT * FROM questions WHERE id = ?",
            (question_id,)
        )

        row = cursor.fetchone()

        if row:
            questions.append({
                "id": row[0],
                "question": row[1],
                "options": row[2].split(","),
                "answer": row[3]
            })

    connection.close()
    return questions


# Retrieve previous quiz results
def get_results():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM results ORDER BY id DESC")
    results = cursor.fetchall()

    connection.close()

    return results


# Execute database functions
if __name__ == "__main__":
    create_database()
    insert_questions()
    print("Database created and questions inserted successfully!")
