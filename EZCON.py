import random
import math
command = "blank"
print(" © 2022 EZCON By LukeBlack952 | Version 0.0.3")
print('Type "help" or "list" for the list of commands')
print()
while not command == "stop":
    if command == "blank" or "exit":
        text = input("Console: ")
        if text.upper() == "STOP":
            command = "stop"
        if text.upper() == "CLOSE":
            command = "stop"
        if command == "stop":
            command = "stop"
        else:
            command = "blank"
        help = "Command List/Help: help | list | log | command | calculate | close | stop | rps | auto-count"
        if text.upper() == "LIST":
            command = "help"
            print(help)
        if text.upper() == "HELP":
            command = "help"
            print(help)
        if text.upper() == "AUTO-COUNT":
            while not command == "exit":
                alert = input("This may lag low-end divices, are you sure you want to use it: ")
                if alert.upper() == "YES":
                    text = input("Count to: ")
                    maxNum = int(text)
                    num = 1
                    while num <= maxNum:
                        print("Auto Count: " + str(num))
                        num += 1
                    print("Done!")
                elif alert.upper() == "NO":
                    command = "exit"
        if text.upper() == "RPS":
            while not command == "exit":
                text = input("Choose Between Rock, Paper or Scissors: ")
                if text.upper() == "EXIT":
                    command = "exit"
                if text.upper() == "ROCK":
                    print("You: Rock")
                    bot = random.randint(1, 3)
                    if bot == 1:
                        print("Bot: Rock")
                        print()
                        print("Tie")
                    if bot == 2:
                        print("Bot: Paper")
                        print()
                        print("You Lose :(")
                    if bot == 3:
                        print("Bot: Scissors")
                        print()
                        print("You win! :D")
                if text.upper() == "PAPER":
                    print("You: Paper")
                    bot = random.randint(1, 3)
                    if bot == 1:
                        print("Bot: Rock")
                        print()
                        print("You win! :D")
                    if bot == 2:
                        print("Bot: Paper")
                        print()
                        print("Tie")
                    if bot == 3:
                        print("Bot: Scissors")
                        print()
                        print("You lose :(")
                if text.upper() == "SCISSORS":
                    print("You: Scissors")
                    bot = random.randint(1, 3)
                    if bot == 1:
                        print("Bot: Rock")
                        print()
                        print("You lose :(")
                    if bot == 2:
                        print("Bot: Paper")
                        print()
                        print("You win! :D")
                    if bot == 3:
                        print("Bot: Scissors")
                        print()
                        print("Tie")
        if text.upper() == "LOG":
            while not command == "exit":
                text = input("Log: ")
                if text.upper() == "EXIT":
                    command = "exit"
                else:
                    print('> log("' + text + '")')
                    print(text)
        if text.upper() == "COMMAND":
            while not command == "exit":
                text = input("Command Console: ")
                if text.upper() == "EXIT":
                    command = "exit"
                else:
                    print("> command." + text)
                    help = "Command List/Help: exit"
                if text.upper() == "LIST":
                    print(help)
                if text.upper() == "HELP":
                    print(help)
        if text.upper() == "CALCULATE":
            while not command == "exit":
                text = input("Calc Type (Plus | Minus | Divided By | Times | To the Power | To the Square Root): ")
                if text.upper() == "PLUS":
                    first = input("Number: ")
                    first = str(first)
                    print("> " + first)
                    second = input("Plus: ")
                    second = str(second)
                    print("> " + second)
                    answer = float(first) + float(second)
                    print(float(answer))
                elif text.upper() == "MINUS":
                    first = input("Number: ")
                    first = str(first)
                    print("> " + first)
                    second = input("Minus: ")
                    second = str(second)
                    print("> " + second)
                    answer = float(first) - float(second)
                    print(float(answer))
                elif text.upper() == "DIVIDED BY":
                    first = input("Number: ")
                    first = str(first)
                    print("> " + first)
                    second = input("Divided By: ")
                    second = str(second)
                    print("> " + second)
                    answer = float(first) / float(second)
                    print(float(answer))
                elif text.upper() == "TIMES":
                    first = input("Number: ")
                    first = str(first)
                    print("> " + first)
                    second = input("Times: ")
                    second = str(second)
                    print("> " + second)
                    answer = float(first) * float(second)
                    print(float(answer))
                elif text.upper() == "TO THE POWER":
                    first = input("Number: ")
                    first = str(first)
                    print("> " + first)
                    second = input("To the Power of: ")
                    second = str(second)
                    print("> " + second)
                    answer = float(first) ** float(second)
                    print(float(answer))
                elif text.upper() == "TO THE SQUARE ROOT":
                    first = input("Number: ")
                    first = str(first)
                    print("> " + first)
                    answer = math.sqrt(float(first))
                    print(float(answer))
                if text.upper() == "EXIT":
                    command = "exit"
        else:
            if command == "blank":
                print("Unknown Command.")
