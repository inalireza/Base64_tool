import inquirer  
from colorama import Fore, init 
import base64



print (Fore.LIGHTBLUE_EX,"=============================|START|===============================")
print (Fore.WHITE," ")
questions = [
    inquirer.List('task',
        message="Select Object : ",
        choices=[Fore.GREEN,'Convert Text To Base64' ,'Convert Base64 To Text','Exit' ,],
    ),  
]
while True:  
   
    init(autoreset=False)
   
    answers = inquirer.prompt(questions)
    if answers["task"] == "Convert Text To Base64":
        inp1 = input("Enter Text For Convert To Base64 : ")
        message = inp1
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        print (Fore.WHITE, " ")
        print (Fore.RED,"----------------Convert-Your-Text-To-Base64-DONE-----------------")
        print (Fore.LIGHTGREEN_EX, "Your code :==\n ====>       ",base64_message) 
        print (Fore.LIGHTBLUE_EX, "---------------------END-ENCODING----------------------------- ")

    if answers["task"] == "Convert Base64 To Text":
        inp = input("Enter Base64 For Convert To Text : ")
        message = inp
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64decode(message_bytes)
        base64_message = base64_bytes.decode('ascii')
        print (Fore.RED,"---------------Convert-Your-BASE64-Code-To-text-DONE-------------------")
        print (Fore.LIGHTGREEN_EX, "Your Text :==\n ====>       ", base64_message)
        print (Fore.LIGHTBLUE_EX, "---------------------END-DECODING----------------------------- ")

    if answers["task"] == "Exit":
        break