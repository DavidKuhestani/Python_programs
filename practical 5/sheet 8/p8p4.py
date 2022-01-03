"""
Make seven placeholders for each group
Get input from user
while the user input is bigger or equal to 0 the program should run
if the user input is in one of the categories
    increment the category
prompt user for new integer
if user input < 0
then print the analysis/placeholders
finish program
"""


num_1 = 0
num_2 = 0
num_3 = 0
num_4 = 0
num_5 = 0
num_6 = 0
num_7 = 0


user_output = int(input("Enter integer: "))
while user_output >= 0:
    if user_output < 0:
        break
    elif user_output == 0:
        num_1 += 1
        print("The",user_output, "number is equal to 0")
    elif 0 < user_output <= 20:
        num_2 += 1
        print("The",user_output, "number is greater than 0 and less than or equal to 20")
    elif 20 < user_output <= 40:
        num_3 += 1
        print("The",user_output, "number is greater than 20 and less than or equal to 40")
    elif 40 < user_output <= 60:
        num_4 += 1
        print("The",user_output, "number is greater than 40 and less than or equal to 60")
    elif 60 < user_output <= 80:
        num_5 += 1
        print("The",user_output, "number is greater than 60 and less than or equal to 80")
    elif 80 < user_output <= 100:
        num_6 += 1
        print("The",user_output, "number is greater than 80 and less than or equal to 100")
    else:
        num_7 += 1
        print("The ", user_output, "number is greater than 100")
    user_output = int(input("Enter integer: "))



print("Number is equal to 0:",num_1)
print("Number is greater than 0 and less than or equal to 20:",num_2)
print("Number is greater than 20 and less than or equal to 40:",num_3)
print("Number is greater than 40 and less than or equal to 60:",num_4)
print("Number is greater than 60 and less than or equal to 80:",num_5)
print("Number is greater than 80 and less than or equal to 100:",num_6)
print("Number is greater than 100:",num_7)
print("Program Finished.")