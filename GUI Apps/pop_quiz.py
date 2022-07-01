from tkinter import *
from quiz.quiz_brain import QuizBrain


THEME = "#375362"
RED = "#e7305b"
GREEN = "#9bdeac"

class QuizInterface(): 

    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain

        self.app = Tk() 
        self.app.title('QuizZzZz')
        self.app.config(padx = 20, pady = 20, bg = THEME)
        
        self.score_label = Label(text = 'Score: 0', fg = 'white', bg= THEME)
        self.score_label.grid(row = 0, column = 1)

        self.canvas = Canvas(width = 300, height = 250, bg = 'white')
        self.question_text = self.canvas.create_text(
            150, 125, text = 'Some question text', width = 200,
            fill = THEME, font = ('Arial', 20, 'italic')
            )
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)

        true_img = PhotoImage(file = '/Users/William/Desktop/100_python_projects/py_apps-/GUI Apps/quiz/images/true.png')
        self.true_button = Button(
            image = true_img, highlightthickness=0, highlightbackground= THEME,
            bg = THEME, command = self.true_pressed, activebackground=THEME
            )
        self.true_button.grid(row = 2, column = 0) 
        false_img = PhotoImage(file = '/Users/William/Desktop/100_python_projects/py_apps-/GUI Apps/quiz/images/false.png')
        self.false_button = Button(
            image = false_img, highlightthickness=0, highlightbackground=THEME, 
            bg = THEME, command = self.false_pressed, activebackground=THEME
            )
        self.false_button.grid(row = 2, column = 1) 

        self.get_next_question()

        self.app.mainloop() 

    def get_next_question(self): 
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions(): 
            self.score_label.config(text = f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else: 
            self.canvas.itemconfig(self.question_text, text = "You've reached the end of the quiz" )
            self.true_button.config(state= 'disabled')
            self.false_button.config(state= 'disabled')
            
    def true_pressed(self): 
        # is_right = self.quiz.check_answer('True')  
        self.give_feedback(self.quiz.check_answer('True'))

    def false_pressed(self):   
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right): 
        if is_right: 
            self.canvas.config(bg = GREEN)
        else: 
            self.canvas.config(bg = RED)
        self.app.after(1000, self.get_next_question)