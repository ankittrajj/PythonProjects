#importing modules
import random
import string

print("Welcome to password generator")
# def random_passwd_generator():
while True:

    # asking user for the length of password
    length = int(input("Enter the len of passwd you want!!"))

    # using string module to get lowercase,uppercase,digits,symbols
    lowercase_data = string.ascii_lowercase
    uppercase_data = string.ascii_uppercase
    digits = string.digits
    spcl_char = string.punctuation

    # combining all the data
    combine_data = lowercase_data+uppercase_data+digits+spcl_char

    # creating the password with random module
    initial_password = random.sample(combine_data,length)

    # convert the passwrd into string because before this password is stored in list
    password = "".join(initial_password)
    print(password)


    # after getting one password as output program is giving choice to the user

    option = int(input("Enter the choice 1 or 2 \n1.Need more password\n2.Exit"))
    if option == 2:
        break

        






    # random_passwd_generator()

# random_passwd_generator()

