def converter(number, base):
    value = 0
    i = 1
    while (number != 0):
        value = value + (number % base) * i
        number = int(number / base)
        i = i * 10
    return value



number = int(input("Enter a number in base 10: "))
base = int(input("Enter the base you want the number converted to: "))
print(number, "in base 10 equals", converter(number, base), "in base", base)