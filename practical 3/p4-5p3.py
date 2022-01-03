#program to convert calculate tax due

initial_amount = float(input('What was your income: '))
tax_due1 = initial_amount * 0.60 * 0.23
tax_due2 = initial_amount * 0.40 * 0.41
sum_tax = tax_due1 + tax_due2
total_amount = initial_amount - sum_tax

if initial_amount < 0:
    print('Amount of income must be >= 0. Please try again.')
else:
    print('Initial amount:', round(initial_amount,2))
    print('Tax due with 23%:', round(tax_due1, 2))
    print('Tax due with 41%:', round(tax_due2,2))
    print('Total tax due:', round(sum_tax,2))
    print('Total nett income:', round(total_amount, 2))
