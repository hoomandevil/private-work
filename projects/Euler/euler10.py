def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

sum_primes = 0

for num in range(2, 2000000):
    if is_prime(num):
        sum_primes += num

print(sum_primes)