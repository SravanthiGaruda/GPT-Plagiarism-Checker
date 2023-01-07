from ExtractingQuestionsAndAnswers import *
import difflib
import requests
from helper import auth,tokenMatch

class Plagiarism():
    def PlagiarismChecker(self,file):
        sol = Solution()
        dict_Questions_Answers = sol.ExtractingQuestionsAndAnswers(file)

        percentage_Match = []

        url = "https://api.openai.com/v1/completions"

        for val in dict_Questions_Answers:
            args = {
                'model': 'text-davinci-003',
                'prompt': val,
                'max_tokens': tokenMatch,
            }
            x = requests.post(url = url, json = args, headers={'Authorization' : 'Bearer ' + auth})

            x = x.json()

            GPT_Answer = x['choices'][0]['text']

            User_Answer=dict_Questions_Answers[val]
            seq=difflib.SequenceMatcher(None,GPT_Answer,User_Answer)
            percentage_Match.append(seq.ratio()*100)

        sum = 0
        for percent in percentage_Match:
            sum = sum + percent

        avg = sum / len(percentage_Match)
        return avg

























# dict_Questions_Answers = ExtractingQuestionsAndAnswers()
# # print(dict_Questions_Answers)

# percentage_Match = []

# url = "https://api.openai.com/v1/completions"

# for val in dict_Questions_Answers:
#     args = {
#         'model': 'text-davinci-003',
#         'prompt': val,
#         'max_tokens': tokenMatch,
#     }
#     x = requests.post(url = url, json = args, headers={'Authorization' : 'Bearer ' + auth})

#     x = x.json()
#     # print(x)

#     GPT_Answer = x['choices'][0]['text']

#     User_Answer=dict_Questions_Answers[val]
#     seq=difflib.SequenceMatcher(None,GPT_Answer,User_Answer)
#     percentage_Match.append(seq.ratio()*100)

# sum = 0
# for percent in percentage_Match:
#     sum = sum + percent

# avg = sum / len(percentage_Match)
# print("Plagiarism Matched Percentage ",avg)



# parrot = Parrot(model_tag="prithivida/parrot_paraphraser_on_T5", use_gpu=False)

# parrot = Parrot()

# phrases = ["Can you recommed some upscale restaurants in Newyork?",
#            "What are the famous places we should not miss in Russia?"
# ]

# for phrase in phrases:
#   print("-"*100)
#   print("Input_phrase: ", phrase)
#   print("-"*100)
#   para_phrases = parrot.augment(input_phrase=phrase)
#   for para_phrase in para_phrases:
#    print(para_phrase)