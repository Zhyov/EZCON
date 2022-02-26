command = "blank"
print("         © 2022 EZCON By LukeBlack952")
print('Type "help" or "list" for the list of commands')
print()
while not command == "stop":
    if command == "blank" or "exit":
        text = input("Console: ")
        if text == "stop":
            command = "stop"
        if text == "close":
            command = "stop"
        if command == "stop":
            command = "stop"
        else:
            command = "blank"
        help = "Command List/Help: help | list | log | command | calculate | close | stop"
        if text == "list":
            command = "help"
            print(help)
        if text == "help":
            command = "help"
            print(help)
        if text == "log":
            while not command == "exit":
                text = input("Log: ")
                if text == "exit":
                    command = "exit"
                else:
                    print('> log("' + text + '")')
                    print(text)
        if text == "command":
            while not command == "exit":
                text = input("Command Console: ")
                if text == "exit":
                    command = "exit"
                else:
                    print("> command." + text)
                    help = "Command List/Help: exit"
                if text == "list":
                    print(help)
                if text == "help":
                    print(help)
        if text == "calculate":
            while not command == "exit":
                text = input("Calculation Type (Plus | Minus | Divided By | Times): ")
                if text == "Plus":
                    first = input("First Number: ")
                    first = str(first)
                    print("> " + first)
                    second = input("Second Number: ")
                    second = str(second)
                    print("> " + second)
                    answer = float(first) + float(second)
                    print(float(answer))
                elif text == "Minus":
                    first = input("First Number: ")
                    first = str(first)
                    print("> " + first)
                    second = input("Second Number: ")
                    second = str(second)
                    print("> " + second)
                    answer = float(first) - float(second)
                    print(float(answer))
                elif text == "Divided By":
                    first = input("First Number: ")
                    first = str(first)
                    print("> " + first)
                    second = input("Second Number: ")
                    second = str(second)
                    print("> " + second)
                    answer = float(first) / float(second)
                    print(float(answer))
                elif text == "Times":
                    first = input("First Number: ")
                    first = str(first)
                    print("> " + first)
                    second = input("Second Number: ")
                    second = str(second)
                    print("> " + second)
                    answer = float(first) * float(second)
                    print(float(answer))
                if text == "exit":
                    command = "exit"
        else:
            if command == "blank":
                print("Unknown Command.")
