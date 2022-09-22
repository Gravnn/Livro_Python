peoples = ['Brendon Urie', 'Damiano David', 'Freddie Mercury']
invite = 'I want to invite you for a dinner'

print(peoples[0] + '. ' + invite + '.')
print(peoples[1] + '. ' + invite + '.')
print(peoples[2] + '. ' + invite + '.')

unable = peoples.pop()

print('')

print('Unfortunally ' + unable + " is unable to come to the dinner")

peoples.append("Victoria de Angelis")

print('')

print(peoples[0] + '. ' + invite + '.')
print(peoples[1] + '. ' + invite + '.')
print(peoples[2] + '. ' + invite + '.')

print('')

peoples.insert(0, 'Géssica Xavier')
peoples.append('Geovanna Moreira')
peoples.insert(len(peoples) //2, "Lívia Gomes")

print(peoples[0] + '. ' + invite + '.')
print(peoples[1] + '. ' + invite + '.')
print(peoples[2] + '. ' + invite + '.')
print(peoples[3] + '. ' + invite + '.')
print(peoples[4] + '. ' + invite + '.')
print(peoples[5] + '. ' + invite + '.')

print('')

print('Unfortunally the table is only for three preople')

print('')

print(peoples.pop() + " I'm Really sorry, but you can't go.")
print(peoples.pop() + " I'm Really sorry, but you can't go.")
print(peoples.pop() + " I'm Really sorry, but you can't go.")
print(peoples.pop() + " I'm Really sorry, but you can't go.")

print('')

print(peoples[0] + ". " + invite)
print(peoples[1] + ". " + invite)

del peoples[0]
del peoples[0]

print("")

print(peoples)