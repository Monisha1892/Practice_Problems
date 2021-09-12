print("""Welcome to the car game.
Type commands to start and stop the car.
List of commands will be available when you type help.
Enjoy the game.""")


command = ""
started = False

while True:
    command = input(">").lower()
    if command == 'help':
        print("""start - to start the car
        stop - to stop the car
        quit - to exit""")
    elif command == 'start':
        if started:
            print("car is already started!! what are you doing?")
        else:
            started = True
            print("car started.....ready to go")
    elif command == 'stop':
        if not started:
            print("car is already stopped!! what are you doing?")
        else:
            started = False
            print("car stopped")
    elif command == 'quit':
        print("game ended. thanks for playing")
        break
    else:
        print("i dont understand that...")

