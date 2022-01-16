#Coded By HM
import os
import time
import webbrowser
import random
import pyfiglet

os.system("cls")

welcome = pyfiglet.figlet_format("Rock Paper Scissors By HM", font="slant")
print(welcome)

i = 0
c = 0

while True:
    print("\nThere Are Three Options \nRock = R \nPaper = P \nScissor = S")

    D = ['Rock', 'Paper', 'Scissor']
    usr_in = input("\nWhat is your Choice: ")
    if usr_in == "R":
        usr_in = "Rock"

    elif usr_in == "P":
        usr_in = "Paper"

    elif usr_in == "S":
        usr_in = "Scissor"

    else:
        print("You Entered Wrong Input")
        exit()

    random.shuffle(D)
    cc = D[0]
    print("\nComputer Choosed "+cc)
    print(usr_in + " vs " + cc)

    if cc == usr_in:
        print("Same")

    elif cc == "Rock" and usr_in == "Paper":
        print("You won")
        i = i + 1
        s = str(i) # Convert The Int Into String
        print("\nYour Score Is " + s + "/3\n")

    elif cc == "Rock" and usr_in == "Scissor":
        print("Computer won")
        c = c + 1
        x = str(c)
        print("\nComputer's Score Is " + x + "/3\n")

    elif cc == "Paper" and usr_in == "Rock":
        print("Computer Won")
        c = c + 1
        x = str(c)
        print("\nComputer's Score Is " + x + "/3\n")

    elif cc == "Paper" and usr_in == "Scissor":
        print("You Won")
        i = i + 1
        s = str(i)
        print("\nYour Score Is " + s + "/3\n")

    elif cc == "Scissor" and usr_in == "Paper":
        print("Computer won")
        c = c + 1
        x = str(c)
        print("\nComputer's Score Is " + x + "/3\n")


    elif cc == "Scissor" and usr_in == "Rock":
        print("You Won")
        i = i + 1
        s = str(i)
        print("\nYour Score Is " + s + "/3\n")

    else:
        print("Wrong Choices RE-Run The Code")
        exit()


    if i == 3:
        print("\nYou Won The Game\n")
        os.system("cls")
        print("There Is A Gift For You (Your Web Browser Will Open In 4 Seconds)")
        time.sleep(4)
        webbrowser.open("index.html")
        exit()

    elif c == 3:
        print("\nComputer Won The Game")
        exit()
