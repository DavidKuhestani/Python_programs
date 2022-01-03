"""
Prompt user for input
split stringt into list of substrings
check if user input is not empty
    if dog count equals cat count
        print appearance of words are the same
    else
        print dog words appear x times and cat appears x times
"""

str = input("Enter a string:")
str.lower()
animal_list = str.lower().split()

if str != "":
    if animal_list.count("cat") == animal_list.count("dog"):
        print('dog and cat appears the same number of times.')
    else:
        print('cat appears times', animal_list.count("cat"), 'and dog appears times', animal_list.count("dog"))
