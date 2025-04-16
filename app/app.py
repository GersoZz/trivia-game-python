from trivia import Question, Quiz

def run_quiz():
    print("🎉 ¡Bienvenido al juego de Trivia! 🎉")
    print("🧠 Responde las siguientes preguntas seleccionando la letra de la opción correcta.")

    quiz = Quiz()
    quiz.fetch_questions()

    # Iniciamos la trivia
    while quiz.current_question_index < len(quiz.questions):
        question = quiz.get_next_question()

        if not question:
            break

        print(f"\n❓ Pregunta {quiz.current_question_index}: {question.description}")

        for option in question.options:
            print(option)

        # Capturamos y parseamos la respuesta
        answer = input("✏️ Ingrese su respuesta: ").strip().upper()

        if quiz.answer_question(question, answer):
            print("✅ ¡Correcto! 🎉")
        else:
            print("❌ ¡Incorrecto! 😢")

    print("\n🏁 Juego terminado.")
    print(f"📋 Preguntas contestadas: {quiz.current_question_index}")
    print(f"✔️ Respuestas correctas: {quiz.correct_answers}")
    print(f"❌ Respuestas incorrectas: {quiz.incorrect_answers}")

    total = quiz.correct_answers + quiz.incorrect_answers
    print(f"\n🏆 Tu puntaje es: {quiz.correct_answers}/{total} 🎯")

if __name__ == "__main__":
    run_quiz()
