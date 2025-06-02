import random
import time
chathobby = ["Read", "Dance","Sew","Play games", "Play sports"]
print("Welcome to chatbot")
name = input ("what is your name?")
print("Hello",name,"Nice to meet you!")
hobby = input("What do you like to do?")
time.sleep(2)
print("Thats so cool! I like to", random.choice(chathobby))
day = input("How was your day?")
if day == "Good":
    print("Thats amazing! Me too!")
else: 
    print("Thats okay! Theres always tomorrow!")
print("Its nice chatting with you, see you later!")
