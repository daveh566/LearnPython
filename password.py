# Simple code for creating a specific password and allow the user to input his/her set password in a set number of trials
# Let's say the set password is 1000 and the password limit=the number of times the user will input the password and if they fail it'll return a certain error
# We will allow the user to enter his or her password 
# Code created by Dave KE 2022
# You can run this code in PyCham

password = ("1000")
enter = ""
password_limit = 3
password_count = 0
password_is_wrong = False

while enter != password and not(password_is_wrong) :
    if password_count < password_limit :
        enter = input("Enter password: ")
        password_count += 1
    else :
        password_is_wrong = True
if password_is_wrong:
    print("You blocked the simcard")
else :
    print("Logged in successfully")
