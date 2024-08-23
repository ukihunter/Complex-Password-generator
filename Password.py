import random
import string
import pyperclip
Password_title = input("Password title? ")
output = ""
while True:
    type = input('type? [a = all, n= nombers, l= letters] ')

    if type == 'a':
        for x in range(0,12):
            x = random.choice(string.digits + string.ascii_letters + string.punctuation)
            output += x
        break

    elif type == 'n':
        for x in range(0, 12):
            x = random.choice(string.digits)
            output += x
        break

    elif type == 'l':
        for x in range(0,12):
            x = random.choice(string.ascii_letters)
            output += x
        break

    else:
        print('invalid command')

file_path = r"C:\Users\file_path\Password.txt"
print(output)


try:
    with open(file_path, 'a') as file:
        file.write(f"{Password_title} = {output}\n")
    pyperclip.copy(output)
    print(f"Test file created successfully at {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")




