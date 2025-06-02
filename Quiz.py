import pandas

file_path = "Questions for quiz.xlsx"
reader = pandas.read_excel(file_path)


def play_quiz():

    prev_questions = []
    questions_mark = 0
    good_answer = 0
    bad_answer = 0

    while questions_mark < 5:

        random_row = reader.sample()

        question = random_row.iloc[0, 0]
        try:
            answer = random_row.iloc[0, 1].casefold().strip().replace(" ","")
        except:
            answer = str(random_row.iloc[0, 1])

        if question not in prev_questions:
            prev_questions.append(question)
        else:
            continue

        user_answer = input(question + "\n").casefold().strip().replace(" ","")

        if user_answer == answer:
            good_answer += 1
            print("GOOD ANSWER!")
        else:
            bad_answer += 1
            print("BAD ANSWER!")

        questions_mark += 1

    return good_answer, bad_answer

print("LET'S PLAY 5 QUESTION QUIZ!\n")
result = play_quiz()
print("Your result: ")
print("Good answers : ", result[0])
print("Bad answers: ", result[1])