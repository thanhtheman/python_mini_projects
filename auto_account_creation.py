# This project enables us to create an account (username, password) in 1-step, just by asking the user for his/her email
# the password will be automatically generated.
import string
import random

def email_slicer(email):
    (username, domain) = email.split("@")
    username = username.replace(".","")
    print(f"Your username is: {username}")

characters = list(string.ascii_letters + string.digits + '@$%!#&*^') 

def generate_password():
    password_length = 12    
    random.shuffle(characters)
    password = []
    for i in range(password_length):
        password.append(random.choice(characters))
    password ="".join(password)
    return password

def account_creation():
    print("Welcome to the email slicer!")
    email = input("Please type in your email: ")
    email_slicer(email)
    print(f'Your Password is: {generate_password()}')

account_creation()