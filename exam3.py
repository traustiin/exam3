import tkinter as tk
import sqlite3
from tkinter import messagebox

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Bowl")
        self.root.geometry("400x300")

        self.category_label = tk.Label(root, text="Select Category:")
        self.category_label.pack()

        self.category_var = tk.StringVar(root)
        self.category_var.set("")  # Set default value

        self.category_menu = tk.OptionMenu(root, self.category_var, "Business Ethics", "Business Database Mgmt", "Business Communications", "Principles of Macroeconomics", "Business Applications")
        self.category_menu.pack()

        self.start_button = tk.Button(root, text="Start Quiz Now", command=self.open_quiz_window)
        self.start_button.pack()

    def open_quiz_window(self):
        category = self.category_var.get()
        if not category:
            messagebox.showwarning("Warning", "Please select a category")
            return

        self.quiz_window = tk.Toplevel(self.root)
        self.quiz_window.title("Quiz")
        
        # Connect to the database
        conn = sqlite3.connect('quiz_bowl.db')
        c = conn.cursor()

        # Fetch a question from the selected category
        c.execute('''SELECT question FROM quiz WHERE category = ?''', (category,))
        question = c.fetchone()[0]

        # Close connection
        conn.close()

        self.question_label = tk.Label(self.quiz_window, text=f"Category: {category}\nQuestion: {question}")
        self.question_label.pack()

        # Add drop-down menu for answers
        self.answer_var = tk.StringVar(self.quiz_window)
        self.answer_var.set("")  # Set default value

        self.answer_menu = tk.OptionMenu(self.quiz_window, self.answer_var, "A", "B", "C", "D")
        self.answer_menu.pack()

        self.submit_button = tk.Button(self.quiz_window, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack()

    def check_answer(self):
        answer = self.answer_var.get()
        if not answer:
            messagebox.showwarning("Warning", "Please select an answer")
            return

        # Fetch the correct answer from the database based on the selected category
        category = self.category_var.get()
        if not category:
            messagebox.showwarning("Warning", "Please select a category")
            return

        # Connect to the database
        conn = sqlite3.connect('quiz_bowl.db')
        c = conn.cursor()

        # Fetch the correct answer for the selected category
        c.execute('''SELECT correct_answer FROM quiz WHERE category = ?''', (category,))
        correct_answer = c.fetchone()[0]

        # Close connection
        conn.close()

        # Check if the selected answer matches the correct answer
        if answer == correct_answer:
            messagebox.showinfo("Answer", "Correct")
        else:
            messagebox.showinfo("Answer", "Incorrect")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()



