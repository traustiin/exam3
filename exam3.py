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

        # Fetch question and answers from the selected category
        c.execute('''SELECT question, answer1, answer2, answer3, answer4 FROM quiz WHERE category = ?''', (category,))
        result = c.fetchone()
        if not result:
            messagebox.showerror("Error", "No question found for the selected category")
            conn.close()
            return

        question, *answers = result

        # Close connection
        conn.close()

        # Format answers with letters (A, B, C, D)
        formatted_answers = [f"{chr(65 + i)}. {answer}" for i, answer in enumerate(answers)]

        self.question_label = tk.Label(self.quiz_window, text=f"Category: {category}\nQuestion: {question}")
        self.question_label.pack()

        # Add drop-down menu for answers
        self.answer_var = tk.StringVar(self.quiz_window)
        self.answer_var.set("")  # Set default value

        self.answer_menu = tk.OptionMenu(self.quiz_window, self.answer_var, *formatted_answers)
        self.answer_menu.pack()

        self.submit_button = tk.Button(self.quiz_window, text="Submit Answer", command=self.check_answer)
        self.submit_button.pack()

    def check_answer(self):
        selected_answer = self.answer_var.get()
        if not selected_answer:
            messagebox.showwarning("Warning", "Please select an answer")
            return

        # Fetch the correct answer index from the database based on the selected category
        category = self.category_var.get()
        if not category:
            messagebox.showwarning("Warning", "Please select a category")
            return

        # Connect to the database
        conn = sqlite3.connect('quiz_bowl.db')
        c = conn.cursor()

        # Fetch all answers for the selected category
        c.execute('''SELECT correct_answer, answer1, answer2, answer3, answer4 FROM quiz WHERE category = ?''', (category,))
        answers = c.fetchone()

        # Close connection
        conn.close()

        # Get the index of the correct answer
        correct_index = answers.index(answers[0])

        # Get the index of the selected answer
        selected_index = ord(selected_answer[0]) - ord('A')

        # Check if the selected answer index matches the correct answer index
        if selected_index == correct_index:
            messagebox.showinfo("Answer", "Correct")
        else:
            messagebox.showinfo("Answer", "Incorrect")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()







