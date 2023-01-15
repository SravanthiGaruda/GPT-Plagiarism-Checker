# GPT_Plagiarism_Checker
--------------------------------------------------------------------------------------------------------------------------
GPT Plagiarism Checker is a simple plagiarism tool. If provided with a set of Questions and Answers it will find the similarity between the responses given by GPT and provides a percentage. 

End-Goal of the project:
    - Easy to install and use.
    - Provides percentage of similarity between GPT and student response.
    - Helpfull to professors.

Setting up and Configurataion
--------------------------------------------------------------------------------------------------------------------------
1. Install VScode 
2. Install Python 
3. pip install openai

How to Use
--------------------------------------------------------------------------------------------------------------------------

1. Create a folder which consists of various text files in the format of Question and Answer. (Mock text file has been uploaded in the directort as TestCases.txt for reference).
2. Created folder path needs to be provided in the helper.py file.
3. Create a Authorization Key from https://beta.openai.com/account/api-keys.
4. Provide the created API Key in helper.py file in auth variable.
5. Provide the number of tokens to be matched in the tokenMatch variable present in helper.py file.
6. Run ExtractFilePercentage.py for output.
