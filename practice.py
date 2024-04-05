from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Window Title")

class QuestionAnswer:
    def __init__(self,master,strQuestion,listAnswers,correctAnswer):
        self.correctAnswer = correctAnswer
        self.frameQA = ttk.Frame(master,relief='raised', padding=(5,5))
        self.frameQA.grid()
        self.label1  = ttk.Label(self.frameQA,text=strQuestion)
        self.label1.grid()

        self.answerOptions = ttk.Combobox(self.frameQA)
        self.answerOptions.grid()
        self.answerOptions.config(values=listAnswers)

        self.testButton = ttk.Button(self.frameQA,text="Submit",command=self.checkAnswer)
        self.testButton.grid()
        self.labelFeedback = ttk.Label(self.frameQA)
        self.labelFeedback.grid()
    def checkAnswer (self):
        if self.answerOptions == self.correctAnswer:
            self.labelFeedback.config(text= "Correct!",foreground="green")
        else:
            self.labelFeedback.config(text= "Incorrect!",foreground="red")

listAnswerFromQ1 = ["Green","Blue","Red","Yellow"]
strQuestion1 = "What is austins fav color?"
austinsFavColor = "Green"
q1 = QuestionAnswer(root,strQuestion1,listAnswerFromQ1,austinsFavColor)

strQuestion2 = "What is belles fav color?"
bellesFavColor = "Red"
q2 = QuestionAnswer(root,strQuestion2,listAnswerFromQ1,bellesFavColor)
root.mainloop()