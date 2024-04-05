import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Quiz Bowl Project")
        
        # Create a label for category selection
        self.label = tk.Label(master, text="Select a category:")
        self.label.pack()

        # Create a combobox for category selection
        self.category_var = tk.StringVar()
        self.category_var.set("Select Category")
        self.category_dropdown = tk.OptionMenu(master, self.category_var, "Business Ethics", "Business Database Mgmt", "Business Communications", "Principles of Macroeconomics", "Business Applications")
        self.category_dropdown.pack()

        # Create a button to start the quiz
        self.start_button = tk.Button(master, text="Start Quiz Now", command=self.start_quiz)
        self.start_button.pack()

    def start_quiz(self):
        # Get the selected category
        selected_category = self.category_var.get()
        if selected_category == "Select Category":
            messagebox.showwarning("Warning", "Please select a category!")
        else:
            # Open the second window for the quiz
            self.open_quiz_window(selected_category)

    def open_quiz_window(self, category):
        # Create the second window for the quiz
        self.quiz_window = tk.Toplevel(self.master)
        self.quiz_window.title("Quiz - " + category)

        # Display sample quiz questions and answers for "Business Ethics" category
        if category == "Business Ethics":
            self.questions = [
                "1. What is the definition of business ethics?",
                "2. What are the key principles of ethical decision making in business?"
            ]
            self.correct_answers = [
                "The application of ethical values to business activities",
                "Honesty, fairness, integrity"
            ]
            self.answers = [
                ["The study of how to maximize profits", "The application of ethical values to business activities", "The process of marketing products", "The study of corporate law"],
                ["Honesty, fairness, integrity", "Profit maximization at all costs", "Taking advantage of competitors", "Exploiting workers"]
            ]
            
            self.current_question_index = 0
            self.display_question()

    def display_question(self):
        # Display the current question
        question_label = tk.Label(self.quiz_window, text=self.questions[self.current_question_index])
        question_label.pack()

        # Display answer choices as dropdown menus
        answer_var = tk.StringVar()
        answer_var.set("Select Answer")
        answer_dropdown = tk.OptionMenu(self.quiz_window, answer_var, *self.answers[self.current_question_index])
        answer_dropdown.pack()

        # Add a button to submit the answer
        submit_button = tk.Button(self.quiz_window, text="Submit Answer", command=lambda: self.submit_answer(answer_var.get()))
        submit_button.pack()

    def submit_answer(self, selected_answer):
        # Compare selected answer with correct answer
        if selected_answer == self.correct_answers[self.current_question_index]:
            print(f"Question {self.current_question_index + 1}: Correct")
        else:
            print(f"Question {self.current_question_index + 1}: Incorrect")

        # Move to the next question or finish the quiz
        self.current_question_index += 1
        if self.current_question_index < len(self.questions):
            # Clear current question and display the next question
            for widget in self.quiz_window.winfo_children():
                widget.destroy()
            self.display_question()
        else:
            # End of quiz
            messagebox.showinfo("Quiz Finished", "Quiz Finished! Thank you for participating.")
            self.quiz_window.destroy()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()


