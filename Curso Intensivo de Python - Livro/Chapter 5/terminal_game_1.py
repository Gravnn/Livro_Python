import random

classes = ['archer', 'warrior', 'ladin', 'mage', 'paladin']

print("Type your name")
name = str(input())

print("Choose your class")
print("1_ " + classes[0])
print("2_ " + classes[1])
print("3_ " + classes[2])
print("4_ " + classes[3])
print("5_ " + classes[4])

playerClass = int(input())
welcome = " is in town. Welcome "
if playerClass == 1:
    print("The new " + str(classes[playerClass - 1].lower()) + welcome + name.title().strip() + "!")
if playerClass == 2:
    print("The new " + str(classes[playerClass - 1].lower()) + welcome + name.title().strip() + "!")
if playerClass == 3:
    print("The new " + str(classes[playerClass - 1].lower()) + welcome + name.title().strip() + "!")
if playerClass == 4:
    print("The new " + str(classes[playerClass - 1].lower()) + welcome + name.title().strip() + "!")
if playerClass == 5:
    print("The new " + str(classes[playerClass - 1].lower()) + welcome + name.title().strip() + "!")