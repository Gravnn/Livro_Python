import random

classes = ['archer', 'warrior', 'ladin', 'mage', 'paladin']

print("Type your name")
name = str(input())


print("Choose your class")

for n in range(len(classes)):
    print(str(n + 1) + "_ " + classes[n].title())

player_class = int(input()) -1
print("Welcome " + name.title().strip() + ". The " + classes[player_class] + "!")

