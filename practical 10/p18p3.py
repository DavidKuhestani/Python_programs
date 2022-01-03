"""
Define function
    split string into list with substrings
    initialize count = 0
    loop through each word in list
        if the word is alphabetic and first two characters "co" and last element "e" then
            increment count
    return count

get user input
print(call function)
"""
def string_match(s):
    list = s.split()
    count = 0
    for word in list:
        if (len(word) == 4 and word.isalpha() and word[:2] == 'co' and word[3] == 'e'):
            count +=1
    return count

# if element == 'code':
         #   count += 1

string = input("Enter a string: ")
print("The count of the word code with any letter in the 2nd index is:", string_match(string))