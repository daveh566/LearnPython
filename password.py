
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
