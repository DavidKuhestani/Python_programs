"""
define a function for fibonacci sequence
    if n equals 0 then return 0
    elif n equals 1 return n
    else return fib(n-1) + fib(n-2)

get user input
if user_input is larger or equal to 0 then
    for loop to iterate arguments to the function
        print fibonacci sequence
    prompt user for another input
"""


#Task A and print calls are for task C (demonstration purposes)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return n
    else:
        #Task C) print(n) - include this print statement to see the progress towards basecase
        return fib(n-1) + fib(n-2)


#Task B)
user_input = int(input("Enter a non-negative INT: "))
while user_input >= 0:
    #Input positive single argument to get Fibonacci sequence
    #(user_input + 1) taking into consideration f(0) = 0, f(1) = 1, f(2) = 1 etc..
    for i in range(user_input + 1):
        print(fib(i), end=" ")
    user_input = int(input("\nEnter a non-negative INT: "))