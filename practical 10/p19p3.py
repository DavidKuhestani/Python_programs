"""
Open file
Make a list of the content in the file
Loop through the rows and the chars
Count the occurences of the symbols
Calculate if the modulo of the symbols equal zero
if they do then they are balanced,
if not they are not balanced.

"""

import re
from collections import Counter

f = open("textp19p3.txt")
content = f.readlines()

counter_equal_symbol = 0
counter_square_brackets = 0
counter_parantheses = 0
counter_curly_brackets = 0
for row in content:
    for char in row:
        if char == '<':
            counter_equal_symbol += 1
        if char == '>':
            counter_equal_symbol += 1
        if char == '(':
            counter_parantheses += 1
        if char == ')':
            counter_parantheses += 1
        if char == '{':
            counter_curly_brackets += 1
        if char == '{':
            counter_curly_brackets += 1
        if char == ']':
            counter_square_brackets += 1
        if char == '[':
            counter_square_brackets += 1

if counter_parantheses % 2 == 0:
    print("The total number of parantheses are", counter_parantheses, "and they are balanced.")
else:
    print("The total number of parantheses are", counter_parantheses, "and they are not balanced.")

if counter_equal_symbol % 2 == 0:
    print("The total number of equal signs are:", counter_equal_symbol, "and they are balanced.")
else:
    print("The total number of equal signs are:", counter_equal_symbol, "and they are not balanced.")

if counter_square_brackets % 2 == 0:
    print("The total number of square brackets are:", counter_square_brackets, "and they are balanced.")
else:
    print("The total number of square brackets are:", counter_square_brackets, "and they are not balanced.")

if counter_curly_brackets % 2 == 0:
    print("The total number of curly brackets are:", counter_curly_brackets, "and they are balanced.")
else:
    print("The total number of curly brackets are:", counter_curly_brackets, "and they are not balanced.")







