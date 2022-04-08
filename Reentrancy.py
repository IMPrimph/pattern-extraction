import re
import os

regexStrings = [
    "^function",
    "message.sender.call.value|msg.sender.call.value",
    "call.value|call.val",
    # "msg.sender",
    "[a-zA-Z]+\[[^\]]*]",
    "balance|amount|value"
]

patterns = []

files = os.listdir('./fold/recy/')
inputFileDir = './fold/recy/'
outputFileDir = './op/recy/'


def writeToFile(pathToFile, text):
    modeToWrite = 'a'
    num_lines = sum(1 for line in open(pathToFile))
    if num_lines == 0:
        modeToWrite = 'w'
    file = open(pathToFile, modeToWrite)
    file.write(text)
    file.close()
    return


def checkPatterns(f):
    with open(inputFileDir + f) as file:
        for sentence in file:
            sentence = sentence.strip().lower()
            sentence = re.sub("\s", "", sentence)
            # writeToFile(outputFileDir + f, sentence)
            for s in regexStrings:
                x = re.findall(s, sentence, re.IGNORECASE)
                if(x):
                    patterns.append(sentence)
                    # patterns.append(s)
                    # patterns.append('\n')
        temp = "\n".join(patterns)
        writeToFile('./REPatterns.txt', temp)
        # writeToFile(outputFileDir + f, temp)
        patterns.clear()


for file in files:
    checkPatterns(file)

# print(patterns)
