town_from_user = input('Type a town/city: ')

if town_from_user == 'Dublin' or town_from_user == 'Kilkenny':
    print('You entered ' + town_from_user + '. ' + town_from_user + ' is in Leinster.')
elif town_from_user == 'Belfast' or town_from_user == 'Derry' or town_from_user == 'Lisburn':
    print('You entered ' + town_from_user + '. ' + town_from_user + ' is in Ulster.')
elif town_from_user == 'Cork' or town_from_user == 'Waterford' or town_from_user == 'Limerick':
    print('You entered ' + town_from_user + '. ' + town_from_user + ' is in Munster.')
elif town_from_user == 'Slige' or town_from_user == 'Galway':
    print('You entered ' + town_from_user + '. ' + town_from_user + ' is in Connaught.')
else:
    print("Sorry, I didn't recognize that name.")

