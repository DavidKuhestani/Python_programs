#Prompt user for name
#If name is Mickey Mouse or Spongebob Square pants --> Print "I am not sure that is your name"
#If user enters David, print "That is a cool name"
#otherwise print out that the user has a nice name

my_name = 'David'
name_1 = 'Spongebob Squarepants'
name_2 = 'Mickey Mouse'

name = input('Enter your name: ')

if name == name_1 or name == name_2:
    print('I am not sure that is your name..')
elif name == my_name:
    print('That is a cool name')
else:
    print('You have a nice name!')
