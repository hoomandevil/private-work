def calc(first, actions, second):
    """this is a calculation function that 
    can do some simple math"""  #this is _Docstings_ that explains functions while crosshair is inside Parentheses
    if actions == "*":
        return first * second
    elif actions == "/":
        return first / second
    elif actions == "+":
        return first + second
    elif actions == "-":
        return first - second

first_number = int(input("enter first number: "))
calculating = False
while not calculating:
    action = input(" /\n *\n +\n -\n pick an operation: ")
    second_number = int(input("enter second number: "))
    result = calc(first_number, action, second_number)
    print(f"{first_number} {action} {second_number} = {result}")
    keep_going = input("y/n?\n")
    if keep_going =="n":
        calculating = True
    else:
        first_number = result
