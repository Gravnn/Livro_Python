import random

classes = ['rogue', 'warrior', 'ladin', 'mage', 'paladin']

print("Whats your complete name?")

name = str(input())

player_class = classes[(random.randrange(len(classes)))]
welcome = '\tThe new ' + str(player_class) + ' in town is!'
print(welcome + ' ' + name.title().strip() + "!")