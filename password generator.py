import random
import string

print("Welcome to password generator")
# def random_passwd_generator():
while True:

    length = int(input("Enter the len of passwd you want!!"))

    lowercase_data = string.ascii_lowercase
    uppercase_data = string.ascii_uppercase
    digits = string.digits
    spcl_char = string.punctuation

    combine_data = lowercase_data+uppercase_data+digits+spcl_char

    initial_password = random.sample(combine_data,length)
    password = "".join(initial_password)
    print(password)

    option = int(input("Enter the choice 1 or 2 \n1.Need more password\n2.Exit"))
    if option == 2:
        break
    # random_passwd_generator()

# random_passwd_generator()

