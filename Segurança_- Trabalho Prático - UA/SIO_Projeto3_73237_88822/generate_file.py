import string
import random

def user():
    letters_digits = string.ascii_letters + string.digits #nao inclui " "
    return ''.join(random.choice(letters_digits) for i in range(int(random.random()*7+3)))

def password():
    password_characters = string.ascii_letters + string.digits + string.punctuation #tmb nao inclui " "
    return ''.join(random.choice(password_characters) for i in range(int(random.random()*15+5)))

#primeira linha tem user01, segunda password01, terceira user02, e por aí adiante
file=open('users.txt','w')
for data in range(int(random.random()*999+1)):
	file.write(str(user())+'\n')
	file.write(str(password())+'\n')
file.close()
