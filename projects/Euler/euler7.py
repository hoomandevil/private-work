def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

count = 0
num = 2

while count < 10001:
    if is_prime(num):
        count += 1
        if count == 10001:
            print(num)
            break
    num += 1