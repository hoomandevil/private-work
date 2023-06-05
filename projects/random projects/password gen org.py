import string
import random

letter = list(string.ascii_letters)
number = list(range(10))
symbol = ["!", "#", "$", "%", "&", "*", "(", ")", "+"]

user_letter = int(input("how many letters do you want?\n"))
user_number = int(input("how many number do you want?\n"))
user_symbol = int(input("how many symbol do you want?\n"))

password = ""
for char in range(1, user_letter + 1):
    password += random.choice(letter)
for char in range(1, user_number + 1):
    password += str(random.choice(number))
for char in range(1, user_symbol + 1):
    password += random.choice(symbol)

new_password = "".join(random.sample(password,len(password)))


print(password)
print(new_password)
