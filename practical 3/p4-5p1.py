#program that converts a currency to another

amount_euro = float(input('Input amount of Euro here: '))
exchange_rate = float(10.85)
amount_nok = amount_euro * exchange_rate

if amount_euro < 0:
    print('Amount must be >= 0. Please try again.')
else:
    print('Amount of NOK:', amount_nok)