from trivia import Question, Quiz

def run_quiz():
    # Creamos las preguntas
    q1 = Question("¿Cuánto es 2 x 4?", ["A) 2", "B) 4", "C) 6", "D) 8"], "D")
    q2 = Question("¿Cuánto es 5 x 6?", ["A) 11", "B) 30", "C) 56", "D) 26"], "B")
    q3 = Question("¿Cuánto es 3 x 3?", ["A) 9", "B) 2", "C) 4", "D) 1"], "A")
    q4 = Question("¿Cuánto es 2 x 2?", ["A) 2", "B) 4", "C) 6", "D) 8"], "B")
    q5 = Question("¿Cuánto es 5 x 5?", ["A) 11", "B) 30", "C) 56", "D) 25"], "D")
    q6 = Question("¿Cuánto es 3 x 4?", ["A) 9", "B) 2", "C) 12", "D) 1"], "C")
    q7 = Question("¿Cuánto es 2 x 3?", ["A) 2", "B) 4", "C) 6", "D) 8"], "C")
    q8 = Question("¿Cuánto es 5 x 4?", ["A) 11", "B) 20", "C) 56", "D) 25"], "B")
    q9 = Question("¿Cuánto es 3 x 5?", ["A) 9", "B) 2", "C) 15", "D) 1"], "C")
    q10 = Question("¿Cuánto es 2 x 5?", ["A) 2", "B) 4", "C) 6", "D) 10"], "D")

    # Creamos la trivia
    quiz = Quiz()
    quiz.add_question(q1)
    quiz.add_question(q2)
    quiz.add_question(q3)
    quiz.add_question(q4)
    quiz.add_question(q5)
    quiz.add_question(q6)
    quiz.add_question(q7)
    quiz.add_question(q8)
    quiz.add_question(q9)
    quiz.add_question(q10)

    # Iniciamos la trivia

    while True:
        question = quiz.get_next_question()

        if not question:
            break

        print("\n" + question.description)
        for option in question.options:
            print(option)

        # Capturamos y parseamos la respuesta
        answer = input("Ingrese su respuesta: ").strip().upper()

        if quiz.answer_question(question, answer):
            print("¡Correcto!")
        else:
            print("¡Incorrecto!")

    total = quiz.correct_answers + quiz.incorrect_answers
    print(f"\nTu puntaje es {quiz.correct_answers}/{total}")

if __name__ == "__main__":
    run_quiz()
