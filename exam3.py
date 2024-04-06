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

        # Close the root window
        self.root.destroy()

        # Connect to the database
        conn = sqlite3.connect('quiz_bowl.db')
        c = conn.cursor()

        # Fetch all questions and answers from the selected category
        c.execute('''SELECT question, answer1, answer2, answer3, answer4 FROM quiz WHERE category = ?''', (category,))
        questions = c.fetchall()
        if not questions:
            messagebox.showerror("Error", "No questions found for the selected category")
            conn.close()
            return

        # Close connection
        conn.close()

        # Initialize quiz window
        self.quiz_window = tk.Tk()
        self.quiz_window.title("Quiz")

        # Store questions and answers
        self.questions = questions
        self.current_question_index = 0

        # Display first question
        self.display_question()

    def display_question(self):
        question, *answers = self.questions[self.current_question_index]

        # Format answers with letters (A, B, C, D)
        formatted_answers = [f"{chr(65 + i)}. {answer}" for i, answer in enumerate(answers)]

        # Display question number
        question_number = self.current_question_index + 1
        self.question_label = tk.Label(self.quiz_window, text=f"Question {question_number}: {question}", font=("Helvetica", 12, "bold"))
        self.question_label.pack()

        # Add drop-down menu for answers
        self.answer_var = tk.StringVar(self.quiz_window)
        self.answer_var.set("")  # Set default value

        self.answer_menu = tk.OptionMenu(self.quiz_window, self.answer_var, *formatted_answers)
        self.answer_menu.config(font=("Helvetica", 10))
        self.answer_menu.pack()

        self.submit_button = tk.Button(self.quiz_window, text="Submit Answer", command=self.check_answer, font=("Helvetica", 10, "bold"), bg="blue", fg="white")
        self.submit_button.pack()

    def check_answer(self):
        selected_answer = self.answer_var.get()
        if not selected_answer:
            messagebox.showwarning("Warning", "Please select an answer")
            return

        # Get the index of the selected answer
        selected_index = ord(selected_answer[0]) - ord('A')

        correct_index = 0  # Assuming the first answer is always correct
        if selected_index == correct_index:
            messagebox.showinfo("Answer", "Correct")
        else:
            messagebox.showinfo("Answer", "Incorrect")

        # Move to the next question
        self.current_question_index += 1

        # Check if there are more questions
        if self.current_question_index < len(self.questions):
            # Remove the current question widgets
            self.question_label.pack_forget()
            self.answer_menu.pack_forget()
            self.submit_button.pack_forget()
            # Display the next question
            self.display_question()
        else:
            messagebox.showinfo("End of Quiz", "You have completed all questions")
            # Close the quiz window
            self.quiz_window.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

