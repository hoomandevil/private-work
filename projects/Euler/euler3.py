sum = 1
for x in range(2, 600851475143):
    isprime = True
    for y in range(2, x):
        if x % y == 0:
            isprime = False
    if isprime == False:
        continue
    if 600851475143 % x == 0:
        sum *= x
        print(x, "yes", sum)