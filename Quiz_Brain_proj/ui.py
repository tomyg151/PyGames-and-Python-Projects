from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_Label = Label(text=f"score: 0", fg="white", bg=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.score_Label.grid(row=1, column=2)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Some Question Text", fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"),
                                                     width=280)  # the width 200 is less then 300 so the text could
        # fill easily in the canvas
        self.canvas.grid(row=2, column=1, columnspan=2, pady=50)

        # Buttons
        self.cross_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.cross_image, highlightthickness=0,
                                   command=self.false_pressed)
        self.false_button.grid(row=3, column=2)
        self.right_mark_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.right_mark_image, highlightthickness=0,
                                  command=self.true_pressed)
        self.true_button.grid(row=3, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_Label.config(text=f"score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disable")
            self.false_button.config(state="disable")

def true_pressed(self):
    self.grt_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.grt_feedback(self.quiz.check_answer("False"))

    def grt_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)  # we must use after method when using a
        # mainloop because time dont sleep will not work in this situations.
