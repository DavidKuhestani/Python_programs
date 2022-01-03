animals = 'herd of elephants'

print('Segment is:', animals[0:-1])

#(a) = when x and y are the same nothing prints. The reason is we are slicing from a speicfic Index to a specific index, when they are the same, it means one index is both the start and end.
#(b) = when x is great than y, it does not print anything as well. Reason for this is x which is the starting points and y which is until a index but not including. It´s reverse, meaning nothing will be printed.
#(c) = when x is omitted it is the same as the starting index [:y] == [0:y]
#(d) = when y is omitted it means until the last index [x:] == [x:-1]
#(e) = when x and y is omitted then it prints the whole string