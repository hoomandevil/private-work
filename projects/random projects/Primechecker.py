def prime_checker(number):
    isprime = True
    for remainder in range(2, number):
        if number % remainder == 0:
            isprime = False
    if isprime:
        print("it is prime")
    else:
        print("it is not prime")


n = int(input("check this number: "))

prime_checker(number=n)


#################################################
sum = 0
for x in range(2, 2000001):
    isprime = True
    for y in range(2, x):
        if x % y == 0:
            isprime = False
    if isprime:
        sum += x
        #print(x)
print(sum)
