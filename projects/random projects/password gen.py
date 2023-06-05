import string
import random

letter = list(string.ascii_letters)
number = list(range(10))
symbol = ["!", "#", "$", "%", "&", "*", "(", ")", "+"]

user_letter = int(input("how many letters do you want?\n"))
user_number = int(input("how many number do you want?\n"))
user_symbol = int(input("how many symbol do you want?\n"))

letters = random.choices(letter, k=user_letter)
numbers = random.choices(number, k=user_number)
symbols = random.choices(symbol, k=user_symbol)

temp_password = letters + numbers + symbols
str_password = "".join(map(str, temp_password))
password = ''.join(random.sample(str_password, len(str_password)))

print(temp_password)
print(str_password)
print(password)
