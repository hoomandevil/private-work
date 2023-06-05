from replit import clear
bids = {}
def append(keys, values):
    bids.update({key: value})

biding_finished = False
while not biding_finished:
    key = input("What is your name:\n")
    value = int(input("How much do you want to bid:\n$"))
    append(keys=key, values=value)
    biding = input("do you want to bid? y/n\n").lower()
    if biding == "n":
        biding_finished = True
    else:
        clear()

winner = sorted(bids.items(), key=lambda x: x[1], reverse=True)

print(winner)
print(f"winner is {winner[0][0]} with bid of {winner[0][1]}$")