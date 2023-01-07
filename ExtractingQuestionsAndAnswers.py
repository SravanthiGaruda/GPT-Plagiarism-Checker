import itertools

class Solution():
    def ExtractingQuestionsAndAnswers(self,file):

        dict_Questions_Answers = {}
        questions = []
        answers = []

        with open(file) as file:
            for line in file:

                if not line:
                    continue
                elif 'Question' in line:
                    questions.append(line)
        
        with open('TestCases2.txt') as file:
            for line in file:
 
                if not line:
                    continue
                elif 'Answer' in line:
                    answers.append(line)

        for (question, ans) in itertools.zip_longest(questions, answers):
            dict_Questions_Answers[question] = ans

        return dict_Questions_Answers
