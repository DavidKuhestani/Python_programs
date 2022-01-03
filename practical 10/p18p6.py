"""
Open file in read mode
Initialize count to zero
Loop through each rows in the file
    Detect patterns
        increment counter
close file
create new file named results.txt and write counter there.
Close file
"""

import re

filename = open("random.mhtml", "r")

file = filename.readlines()

count_one = 0

for row in file:
    pattern_one = re.findall(r"<!--|-->|<|>|e|\n", row)
    if pattern_one:
        print(pattern_one)
        print(row)
        count_one += len(pattern_one)


print(count_one)
filename.close()

with open("results.txt", "w") as fp:
    fp.write("The count value is {}".format(count_one))

