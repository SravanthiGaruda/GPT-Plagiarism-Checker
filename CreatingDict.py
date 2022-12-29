import itertools

def CreatingDict():

    dict_Questions_Answers = {}
    questions = []
    answers = []
    with open('TestCases2.txt') as file:
        for line in file:
            # print(line)
            if not line:
                continue
            elif 'Question' in line:
                questions.append(line)
    
    with open('TestCases2.txt') as file:
        for line in file:
            # print(line)
            if not line:
                continue
            elif 'Answer' in line:
                answers.append(line)

    for (question, ans) in itertools.zip_longest(questions, answers):
        dict_Questions_Answers[question] = ans

    # print(dict_Questions_Answers)

    return dict_Questions_Answers

CreatingDict()