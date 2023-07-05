import random

class Player:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.point=0

# klasa Quiz
class Quiz:
    def __init__(self):
        self.question_pool=[]
        self.quantity_of_questions=0
        self.remaining_questions=0

    # dodaj pytanie
    def add_question(self,question):
        self.question_pool.append(question)
        self.quantity_of_questions+=1

    # rozpocznij_gre
    def start_the_game(self):
        points=0
        random.shuffle(self.question_pool)
        self.remaining_questions = self.quantity_of_questions
        for question,answer in self.question_pool:
            print(question)
            answer=input("Put the answer: ")
            if answer==question[1]:
                points+=1
                print("Congrats!!! Good answer")
            else:
                print("Unfortunately!!! Bad answer")

            self.remaining_questions-=1
            print(f"Number of points: {points}")
            print(f"Remaining questions: {self.quantity_of_questions}")

        print("End of the game!!")
        if points>self.question_pool/2:
            print("Congrats, You won")
        else:
            print("I am sorry, You failed")

        self.keep_playing()
    def keep_playing(self):
        decision=input("Do You wanna keep playing?")
        if decision.lower()=="Yes":
            self.start_the_game()
        else:
            print("Thanks for playing!")

# Przykładowe pytania
pytanie1 = ("Jaki jest stolica Polski?", "Warszawa")
pytanie2 = ("Ile wynosi pierwiastek kwadratowy z 16?", "4")
pytanie3 = ("Która planeta jest trzecia od Słońca?", "Ziemia")

# Stworzenie obiektu Quiz
quiz = Quiz()

# Dodanie pytań do puli
quiz.add_question(pytanie1)
quiz.add_question(pytanie2)
quiz.add_question(pytanie3)

# Rozpoczęcie gry
quiz.start_the_game()