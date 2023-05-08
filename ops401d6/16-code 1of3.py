#!/user/bin/python3
import time

mode = input("Select mode: 1) Offensive; Dictionary Iterator 2) Defensive; Password Recognized
")

if mode == "1":
    file_path = input("Enter word list file path: ")
    with open(file_path, "r") as file:
        for line in file:
            word = line.strip()
            print(word)
            time.sleep(1)

elif mode == "2":
    user_input = input("Enter string: ")
    file_path = input("Enter word list file path: ")
    with open(file_path, "r") as file:
        words = file.read().splitlines()
        if user_input in words:
            print("Password recognized.")
        else:
            print("Password not found in word list.")
else:
    print("Invalid mode selected.")
# source: chat gbt