def ispan(n):
    return str(n) == str(n)[::-1]
max_number = 0
for x in range(100, 1000):
    for y in range(x+1, 1000):
        number = x * y
        if ispan(number) and number > max_number:
            max_number = number
print(max_number)