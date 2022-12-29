from CreatingDict import *
import difflib
import requests

dict_Questions_Answers = CreatingDict()
# print(dict_Questions_Answers)

percentage_Match = []

url = "https://api.openai.com/v1/completions"

for val in dict_Questions_Answers:
    args = {
        'model': 'text-davinci-003',
        'prompt': val,
        'max_tokens': 13,
    }
    x = requests.post(url = url, json = args, headers={'Authorization' : 'Bearer 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'})

    x = x.json()
    # print (x)
    # print(x['choices'][0]['text'])

    GPT_Answer = x['choices'][0]['text']

    User_Answer=dict_Questions_Answers[val]
    seq=difflib.SequenceMatcher(None,GPT_Answer,User_Answer)
    percentage_Match.append(seq.ratio()*100)

    # print(percentage_Match)

sum = 0
for percent in percentage_Match:
    sum = sum + percent

avg = sum / len(percentage_Match)
print("Plagiarism Matched Percentage ",avg)