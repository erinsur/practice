import os
import time
import random
import string

print("\nCustomize your password.\n")
pass_length = int(input("Enter password length: "))
pass_type = (input("u = upper only; l = lower only; b = both upper and lower: ")).lower()

if pass_type == "u":
    user_pass = (''.join(random.choices(string.ascii_letters, k=pass_length))).upper()
elif pass_type == "l":
    user_pass = (''.join(random.choices(string.ascii_letters, k=pass_length))).lower()
else:
    user_pass = ''.join(random.choices(string.ascii_letters, k=pass_length))

print(f"Memorize this password: {user_pass}")
time.sleep(1.5)
os.system('cls' if os.name == 'nt' else 'clear')

user_guessed = False

#ask for the password - give 3 tries
user_num_guess = 1
while (user_num_guess <= 3):
    user_curr_guess = input(f"\nAttempt #{user_num_guess} - Enter your password: ")
    if (user_curr_guess == user_pass):
        user_guessed = True
        break
    else:
        user_num_guess += 1

#if unable to give password then you are locked out
#if answered then "you got in!"
if (user_guessed == True):
    print(f"\nYou got in with only {user_num_guess} tries! Awesome work.")
else:
    print(f"\nBoo, you are in jail now. The correct password is {user_pass}")




