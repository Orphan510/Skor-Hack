import itertools
import string
import time
from termcolor import colored
import pyfiglet
import os 
os.system ("clear")
def password_cracker(target_password):
    chars = string.ascii_letters + string.digits + string.punctuation
    attempts = 0

    for length in range(4, 9):  
        for guess in itertools.product(chars, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == target_password:
                print(colored(f"The password has been guessed '{guess}' in {attempts} attempts.", 'green'))
                return guess, attempts
            else:
                print(colored(f"Wrong guess: {guess}", 'red'))
                time.sleep(0.1)  

    return None, attempts

if __name__ == "__main__":
    ascii_art = pyfiglet.figlet_format("skor-hack", font="slant")
    print(colored(ascii_art, 'cyan'))
    print("\033[93m Don't forget to follow me on my Instagram account ahu_orphan")
    print()
    input ("\033[92m Enter the account:")
    print ()
    
    target_password = input("\033[92m Enter the guess file: ")
    guessed_password, attempts = password_cracker(target_password)
    
    if not guessed_password:
        print("We couldn't guess the password.")
