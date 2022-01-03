#Prompt user for password for maximum 3 times
#if the password is incorrect, reprompt the user two more times
#if third time is wrong, print you have been denied access
#however, if user prompt correct password, print "you have successfully logged in" and termiante program.

password_attempt = 0
password = 'helloworld'

for i in range(3):
    user_input = input('Enter your password: ')
    if user_input != password:
        password_attempt += 1
        if password_attempt == 3:
            print('you have been denied access')
    elif user_input == password:
        print("You have successfully logged in.")
        break










