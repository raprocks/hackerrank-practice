if __name__=="__main__":
    commands = int(input())
    lst = []
    for _ in range(commands):
        command = input()
        commands = command.split(" ")
        if len(commands) == 1:
            command = commands[0]
            if command == "print":
                print(lst)
            elif command == 'pop':
                lst.pop()
            elif command == 'sort':
                lst.sort()
            elif command == 'reverse':
                lst.reverse()
        elif len(commands) == 2:
            command = commands[0]
            integer = int(commands[1])
            if command == 'remove':
                lst.remove(integer)
            elif command == 'append':
                lst.append(integer)
        elif len(commands) == 3:
            command = commands[0]
            integer = int(commands[2])
            position = int(commands[1])
            if command == 'insert':
                lst.insert(position, integer)
