#Program that calculates initial amount plus taxes
amount = 202048.83
tax_due1 = amount * 0.60 * 0.135
tax_due2 = amount * 0.40 * 0.23
sum_tax = tax_due1 + tax_due2
total_amount = amount + sum_tax
print('The total amount is:', round(total_amount,2))
