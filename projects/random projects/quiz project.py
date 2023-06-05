sum = 0
print("hello and welcome to Quiz")
name = input("plz enter your name: ")
question1 = input("2*2= ")
question2 = input("2*10= ")
question3 = input("10*10= ")
question4 = input("5*10= ")
while 1:
    question1.isdigit(), question2.isdigit(), question3.isdigit(), question4.isdigit()
    break
    quit()
if int(question1) == 4:
    sum += 1
if int(question2) == 20:
    sum += 1
if int(question3) == 100:
    sum += 1
if int(question4) == 50:
     sum += 1
if sum >= 3:
    print("good job! ",name,"your score is ", sum," out of 4")
else:
    print("sorry! you failed the Quiz", name.upper(),"your score is",sum,"out of 4")