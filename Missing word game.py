import random
import time
Choices = ["sad","play","blue"]
print("Welcome to the missing word game")

def question():
    answer = input("\nWhich is the missing word?\nsad\nplay\nblue\n")
    return answer
    
QuestionOne = "Sam likes to _______ games."
print(QuestionOne)
answer = question()
if answer == Choices[1]:
    print("Very good!")
else:
    print("Wrong!")
time.sleep(2)

QuestionTwo = "\nHe was very ______today."
print(QuestionTwo)
answer = question()
if answer == Choices[0]:
    print("Very good!")
else:
    print("Wrong!")
time.sleep(2)

QuestionThree = "\nThe sky is very _____ today."
print (QuestionThree)
answer = question()
if answer == Choices[2]:
    print("Very good!")
else:
    print("Wrong!")


