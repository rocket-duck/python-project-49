def create_game_data(question, answer):
    def f(message):
        if message == "question":
            return question
        if message == "answer":
            return answer

    return f


def get_question(data):
    return data("question")


def get_answer(data):
    return data("answer")
