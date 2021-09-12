# emojii_dict = {
#     ":)" : "😄",
#     ":(" : "😞",
#     ";)" : "😉",
#     ":D" : "😁",
#     ";;)" : "😚",
#     ":P" : "😋",
#     ":x" : "😘",
#     "o:-)" : "😇",
#     "x(" : "😠"
# }
#
# message = input("enter message: ")
# words = message.split(" ")
# output = ""
# for i in words:
#     if i in emojii_dict:
#         output += emojii_dict.get(i) + " "
#     else:
#         output += i + " "
# print(output)


def message_out(user_input):
    emojii_dict = {
        ":)": "😄",
        ":(": "😞",
        ";)": "😉",
        ":D": "😁",
        ";;)": "😚",
        ":P": "😋",
        ":x": "😘",
        "o:-)": "😇",
        "x(": "😠"
    }

    words = user_input.split(" ")
    output = ""
    for i in words:
        if i in emojii_dict:
            output += emojii_dict.get(i) + " "
        else:
            output += i + " "
    return output



message = input("enter message: ")
message_cov = message_out(message)
print(message_cov)


