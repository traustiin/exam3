import tkinter as tk

class CategorySelectionWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Category Selection")
        
        self.label = tk.Label(master, text="Select a category:")
        self.label.pack()
        
        self.category_var = tk.StringVar()
        self.category_var.set("Business Communications")
        
        self.categories = ["Business Communications", "Business Ethics", "Principles of Macroeconomics",
                           "Business Applications", "Business Database MGMT"]
        
        self.category_menu = tk.OptionMenu(master, self.category_var, *self.categories)
        self.category_menu.pack()
        
        self.start_button = tk.Button(master, text="Start Quiz Now", command=self.start_quiz)
        self.start_button.pack()
        
    def start_quiz(self):
        selected_category = self.category_var.get()
        self.master.destroy()  # Close category selection window
        quiz_window = QuizWindow(selected_category)
        quiz_window.show()


class QuizWindow:
    def __init__(self, category):
        self.category = category
        self.master = tk.Tk()
        self.master.title("Quiz: " + self.category)
        
        # Display quiz questions and answers here
        
    def show(self):
        self.master.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = CategorySelectionWindow(root)
    root.mainloop()
