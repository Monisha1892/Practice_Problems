print("""Welcome to the car game.
Type commands to start and stop the car.
List of commands will be available when you type help.
Enjoy the game.""")


command = ""
memory = ""

while True:
    command = input(">").lower()
    if command == memory:
        print(f"car has already {memory}ed. What are you doing?")
    elif command == 'help':
        print("""start - to start the car
        stop - to stop the car
        quit - to exit""")
    elif command == 'start':
        print("car started.....ready to go")
        memory = 'start'
    elif command == 'stop':
        print("car stopped")
        memory = command
    elif command == 'quit':
        print("game ended. thanks for playing")
        break
    else:
        print("i dont understand that...")

