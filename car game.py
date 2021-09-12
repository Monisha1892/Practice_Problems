print("""Welcome to the car game.
Type commands to start and stop the car.
List of commands will be available when you type help.
Enjoy the game.""")


command = input(">")

while command != 'quit':
    if command == 'help':
        print("""start - to start the car
        stop - to stop the car
        quit - to exit""")
        command = input(">")
    elif command == 'start':
        print("car started.....ready to go")
        command = input(">")
    elif command == 'stop':
        print("car stopped")
        command = input(">")
    else:
        print("i dont understand that.....")
        command = input(">")
else:
    print("game ended. thanks for playing")


# print("""Welcome to the car game.
# Type commands to start and stop the car.
# List of commands will be available when you type help.
# Enjoy the game.""")
#
# def game_function(command):
#     while command != 'quit':
#         if command == 'help':
#             print("""start - to start the car
#             stop - to stop the car
#             quit - to exit""")
#             command = input(">")
#             game_function(command)
#         elif command == 'start':
#             print("car started.....ready to go")
#             command = input(">")
#             game_function(command)
#         elif command == 'stop':
#             print("car stopped")
#             command = input(">")
#             game_function(command)
#     else:
#         print("game ended. thanks for playing")
#
# command = input(">")
# game_function(command)

# print("""Welcome to the car game.
# Type commands to start and stop the car.
# List of commands will be available when you type help.
# Enjoy the game.""")
#
# def game_function(command):
#     while command != 'quit':
#         if command == 'help':
#             print("""start - to start the car
#             stop - to stop the car
#             quit - to exit""")
#             command = input(">")
#         elif command == 'start':
#             print("car started.....ready to go")
#             command = input(">")
#         elif command == 'stop':
#             print("car stopped")
#             command = input(">")
#         else:
#             print("i dont understand that....")
#             command = input(">")
#     else:
#         print("game ended. thanks for playing")
#
# command = input(">")
# game_function(command)



