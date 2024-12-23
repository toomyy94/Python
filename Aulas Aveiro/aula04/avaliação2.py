# Complete the code to make the HiLo game...

import random

def main():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101);
    n = 0
    i=0
    # put your code here
    while n!=secret:
        n = int(input("Can you guess my secret?"))
        i=0
        if n<secret:
            print("Low")
        elif n>secret:
            print("High")
        else:
            print("Parabéns, concluiste o desafio")
            i=i+1
            print(i)
main()
