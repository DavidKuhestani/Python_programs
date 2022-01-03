#Prompt the user for a password
#if the password is incorrect print"Please try again" and prompt the user for the password two more times.
#If the password is correct, print "you have successfully logged in and termiante the program.
#However, if the wrong password has been typed 3 times, print you have been denied access".

password = 'helloworld'
password_attempt = 0
correct_password = 0
password_attempt_2 = 0

while password_attempt < 3:
    user_input = input('Type your password: ')
    if user_input == password:
        print('You have successfully logged in!')
        break
    elif user_input != password:
        print('Sorry, the password is wrong. Please type your password three times.')
        while password_attempt_2 <= 3:
            prompt_3 = input("Enter you password: ")
            if prompt_3 == password:
                password_attempt_2 += 1
            else:
                print("Access denied.")
                break
        if password_attempt_2 == 3:
            print('You have successfully logged in!')










