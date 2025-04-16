import requests

API_URL = "http://api:8000"  # Cambia este valor si tu API corre en otro puerto o IP

class Question:
    def __init__(self, id, description, options):
        self.id = id
        self.description = description
        self.options = options

    def is_correct(self, answer):
        try:
            response = requests.post(f"{API_URL}/responder", json={
                "pregunta_id": self.id,
                "respuesta": answer
            })
            response.raise_for_status()
            is_correct = response.json()["is_correct"]
            return is_correct
        except requests.RequestException as e:
            print(f"⚠️ Error al validar respuesta: {e}")
            return False

class Quiz:
    def __init__(self):
        self.questions = []
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0

    def fetch_questions(self):
        try:
            response = requests.get(f"{API_URL}/preguntas")
            response.raise_for_status()
            preguntas_json = response.json()

            for item in preguntas_json:
                opciones = [
                    f"A) {item['opciones']['a']}",
                    f"B) {item['opciones']['b']}",
                    f"C) {item['opciones']['c']}",
                    f"D) {item['opciones']['d']}",
                ]

                question = Question(
                    id=item["id"],
                    description=item["pregunta"],
                    options=opciones
                )

                self.add_question(question)
        except requests.RequestException as e:
            print(f"❌ Error al obtener preguntas: {e}")
            raise SystemExit("No se pudo iniciar el juego por error de conexión con la API.")

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def answer_question(self, question, answer):
        if question.is_correct(answer):
            self.correct_answers += 1
            return True
        else:
            self.incorrect_answers += 1
            return False