import random

stages = ['''
  +_____+
  |     |    
  O     |
 /|\    |
 / \    |
        |
=========
''', '''
  +_____+
  |     |    
  O     |
 /|\    |
 /      |
        |
=========
''', '''
  +_____+
  |     |    
  O     |
 /|\    |
        |
        |
=========
''', '''
  +_____+
  |     |    
  O     |
 /|     |
        |
        |
=========
''', '''
  +_____+
  |     |    
  O     |
  |     |
        |
        |
=========
''', '''
  +_____+
  |     |    
  O     |
        |
        |
        |
=========
''', '''
  +_____+
  |     |    
        |
        |
        |
        |
=========
''']

words = ["camel", "arash", "cat", "volcano", "diamond", "balls","abbas","kitten"]
selected_word = random.choice(words)
#print(selected_word)

lives = 6

display = []
for _ in range(len(selected_word)):
    display += "_"
print(display)

end = False

while not end:
    guess = input("guess the word: ").lower()

    for position in range(len(selected_word)):
        letter = selected_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in selected_word:
        lives -= 1
        if lives == 0:
            end = True
            print("you got hanged!")
    print(display)
    if "_" not in display:
        end = True
        print("you will die another day!")
    print(stages[lives])
print(selected_word)
