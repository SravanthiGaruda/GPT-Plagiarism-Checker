import os
from helper import path
from ExtractingQuestionsAndAnswers import *
from PlagiarismChecker import *
from pathlib import Path

def ExtractFilesPercentage():
    files = Path(path)
    percentageForFiles = {}
    for file in files.iterdir():
        plag = Plagiarism()
        percentageForFiles[file.name] = plag.PlagiarismChecker(file)

    print(percentageForFiles)

ExtractFilesPercentage()