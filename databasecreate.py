import sqlite3

# Connect to the SQLite database (it will create one if it doesn't exist)
conn = sqlite3.connect('questions_answers.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table named DS-3850
cursor.execute('''
CREATE TABLE IF NOT EXISTS "DS-3850" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

# List of questions and answers related to intro to coding
qa_pairs = [
    ("What does 'variable' mean in programming?", "A storage location paired with a name that contains data."),
    ("What is a 'function'?", "A block of code that performs a specific task and can be reused."),
    ("What is an 'if statement'?", "A conditional statement that executes code based on whether a condition is true or false."),
    ("What is 'looping'?", "The process of repeating a block of code multiple times."),
    ("What is 'syntax'?", "The set of rules that defines the combinations of symbols in a programming language."),
    ("What is 'debugging'?", "The process of finding and fixing errors in code."),
    ("What does 'API' stand for?", "Application Programming Interface."),
    ("What is 'data type'?", "A classification that specifies which type of value a variable can hold (e.g., integer, string)."),
    ("What is a 'list' in Python?", "A collection data type that holds an ordered sequence of items."),
    ("What does 'IDE' stand for and what is it?", "Integrated Development Environment, a software application that provides tools for coding, testing, and debugging.")
]

# Insert questions and answers into the table
cursor.executemany('''
INSERT INTO "DS-3850" (question, answer)
VALUES (?, ?)
''', qa_pairs)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Questions and answers related to intro to coding have been stored in the DS-3850 table.")
