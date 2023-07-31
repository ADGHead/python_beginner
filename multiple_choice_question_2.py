questions_prompt = [
    "What is the name of the team that won the 2022 FIFA world cup?\n (a)Argentina\n (b)France\n (c)Brazil\n\n",
    "What is 50 + 40?\n (a)100\n (b)150\n (c)90\n\n",
    "what is the shape of the world?\n (a)oval\n (b)Spherical\n (c)flat\n\n",
    "What is the chemical formula of water?\n (a)O2\n (b)H2O\n (c)O3\n\n",
    "Who is the current president of Nigeria?\n (a)Muhmmadu Buhari\n (b)Bola Ahmed Tinubu\n (c)Shehu Shagari\n\n"
]

from questions_2 import Question
questions = [
    Question(questions_prompt[0], "a"),
    Question(questions_prompt[1], "c"),
    Question(questions_prompt[2], "b"),
    Question(questions_prompt[3], "b"),
    Question(questions_prompt[4], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " out of " + str(len(questions)) )

run_test(questions)