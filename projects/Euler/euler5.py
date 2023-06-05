def is_divisible(num):
    for i in range(1, 21):
        if num % i != 0:
            return False
    return True

i = 1

while True:
    if is_divisible(i):
        print(i)
        break
    i += 1