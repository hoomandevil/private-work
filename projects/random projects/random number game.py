import random
sum = 0
number = random.randint(1, 15)
#print(number)
while True:
    if sum >= 5:
        print("BooM!!! You lost!")
        break
    guess = input("Enter number")
    sum += 1
    if not guess.isdigit():
        print("adad bezan")
        break
    if int(guess) >= 16 or int(guess) <= 0:
        print("kharej az mahdoode adad")
    if int(guess) == number:
        print("it tooks " + str(sum) + " attemps to guess it")
        break