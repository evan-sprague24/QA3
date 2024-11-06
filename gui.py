import tkinter as tk
from tkinter import messagebox

# Function to handle the start quiz button click
def start_quiz():
    selected_topic = topic_var.get()
    
    if selected_topic == "":
        messagebox.showwarning("No Selection", "Please select a topic to start the quiz.")
    else:
        messagebox.showinfo("Quiz Starting", f"Starting quiz on {selected_topic}!")

# Set up the main window
root = tk.Tk()
root.title("Quiz Topic Selection")
root.geometry("400x300")

# Label to show instructions
label = tk.Label(root, text="Please choose a topic to start the quiz:", font=("Arial", 14))
label.pack(pady=20)

# Variable for selected topic
topic_var = tk.StringVar()

# Dropdown menu for topic selection
topic_menu = tk.OptionMenu(root, topic_var, "Coding", "Finance", "Early US History", "Economics", "Computer Forensics")
topic_menu.config(font=("Arial", 12), width=20)
topic_menu.pack(pady=10)

# Start quiz button
start_button = tk.Button(root, text="Start Quiz", font=("Arial", 12), command=start_quiz)
start_button.pack(pady=20)

# Run the GUI loop
root.mainloop()