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
# Create a table named Finance_Questions for intro to finance questions
cursor.execute('''
CREATE TABLE IF NOT EXISTS "Finance_Questions" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

# List of questions and answers related to intro to finance
finance_qa_pairs = [
    ("What is the time value of money?", "The concept that money available today is worth more than the same amount in the future."),
    ("What is a budget?", "A financial plan that outlines expected income and expenses over a specific period."),
    ("What is the difference between assets and liabilities?", "Assets are what you own, while liabilities are what you owe."),
    ("What is a stock?", "A share in the ownership of a company, representing a claim on part of the company’s assets and earnings."),
    ("What is a bond?", "A fixed income instrument that represents a loan made by an investor to a borrower."),
    ("What is interest?", "The cost of borrowing money, usually expressed as a percentage of the amount borrowed."),
    ("What is diversification?", "The practice of spreading investments across different assets to reduce risk."),
    ("What is an investment?", "An asset or item acquired with the goal of generating income or appreciation."),
    ("What is a financial statement?", "A formal record of the financial activities and position of a business, person, or entity."),
    ("What is cash flow?", "The total amount of money being transferred in and out of a business.")
]
cursor.execute('''
CREATE TABLE IF NOT EXISTS "History_Questions" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

# List of questions and answers related to intro to modern U.S. history
history_qa_pairs = [
    ("What was the main cause of the Civil War?", "The primary cause was the dispute over slavery and states' rights."),
    ("What event marked the beginning of the Great Depression?", "The stock market crash of 1929."),
    ("What was the significance of the Brown v. Board of Education decision?", "It declared racial segregation in public schools unconstitutional."),
    ("What did the Civil Rights Act of 1964 achieve?", "It prohibited discrimination based on race, color, religion, sex, or national origin."),
    ("What was Watergate?", "A political scandal involving a break-in at the Democratic National Committee headquarters and the subsequent cover-up."),
    ("Who was the first woman to fly solo across the Atlantic Ocean?", "Amelia Earhart."),
    ("What was the purpose of the New Deal?", "To provide relief, recovery, and reform in response to the Great Depression."),
    ("What did the Marshall Plan aim to do?", "To aid European nations in rebuilding their economies after World War II."),
    ("What was the main outcome of the Vietnam War?", "The fall of Saigon and the unification of Vietnam under communist control."),
    ("What is the significance of September 11, 2001, in U.S. history?", "It was the day of terrorist attacks that led to significant changes in U.S. domestic and foreign policy.")
]
cursor.execute('''
CREATE TABLE IF NOT EXISTS "Economics_Questions" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

# List of questions and answers related to intro to economics
economics_qa_pairs = [
    ("What is economics?", "The study of how individuals and societies allocate scarce resources."),
    ("What is supply and demand?", "A model that explains the relationship between the quantity of a good that producers are willing to sell and the quantity that consumers are willing to buy."),
    ("What is GDP?", "Gross Domestic Product, a measure of the economic performance of a country."),
    ("What is inflation?", "The rate at which the general level of prices for goods and services is rising."),
    ("What is a market economy?", "An economic system where supply and demand guide the production of goods and services."),
    ("What is opportunity cost?", "The loss of potential gain from other alternatives when one alternative is chosen."),
    ("What are the factors of production?", "The resources used to produce goods and services: land, labor, capital, and entrepreneurship."),
    ("What is a monopoly?", "A market structure where a single seller dominates the market."),
    ("What is fiscal policy?", "The use of government spending and taxation to influence the economy."),
    ("What is a recession?", "A period of economic decline typically defined by a decrease in GDP for two consecutive quarters.")
]
cursor.execute('''
CREATE TABLE IF NOT EXISTS "Forensics_Questions" (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
)
''')

# List of questions and answers related to intro to computer forensics
forensics_qa_pairs = [
    ("What is computer forensics?", "The process of collecting, analyzing, and preserving digital evidence."),
    ("What is a digital footprint?", "The trail of data you leave behind when using the internet."),
    ("What are the key steps in the forensic process?", "Identification, preservation, analysis, and presentation of digital evidence."),
    ("What is data recovery?", "The process of salvaging inaccessible or lost data from damaged storage devices."),
    ("What tools are commonly used in computer forensics?", "Software like EnCase, FTK, and Autopsy."),
    ("What is a hash value?", "A unique string generated from data used to verify the integrity of that data."),
    ("What is the difference between active and passive data collection?", "Active data collection involves interacting with the system, while passive collection does not."),
    ("What is chain of custody?", "A process that ensures the evidence is properly handled and preserved."),
    ("What is metadata?", "Data that provides information about other data, such as the creation date of a file."),
    ("Why is encryption important in forensics?", "Encryption can protect sensitive data, but may also pose challenges for accessing evidence.")
]

# Insert questions and answers into the Forensics_Questions table
cursor.executemany('''
INSERT INTO "Forensics_Questions" (question, answer)
VALUES (?, ?)
''', forensics_qa_pairs)
# Insert questions and answers into the Economics_Questions table
####''', economics_qa_pairs)
# Insert questions and answers into the History_Questions table
#cursor.executemany('''
#INSERT INTO "History_Questions" (question, answer)
#VALUES (?, ?)
#'', history_qa_pairs)
# Insert questions and answers into the Finance_Questions table
#cursor.executemany('''
#INSERT INTO "Finance_Questions" (question, answer)
#VALUES (?, ?)
#''', finance_qa_pairs)
# Insert questions and answers into the table
#cursor.executemany('''
#INSERT INTO "DS-3850" (question, answer)
#VALUES (?, ?)
#''', qa_pairs)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Questions and answers related to intro to coding have been stored in the DS-3850 table.")
