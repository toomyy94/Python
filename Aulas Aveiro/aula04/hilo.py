# Complete the code to make the HiLo game...

import random

def main():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101);
    n = 0
    # put your code here
    while n!=secret:
        n = int(input("Can you guess my secret?"))
        if n>secret:
            print("High")
        elif n<secret:
            print("Low")
        else:
            print("Correto")

main()
