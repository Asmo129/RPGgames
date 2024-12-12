
#from Item import 

import time
def conte_a_rebour ():
    for conte_a_rebour in range(1, 4):
        print ('.')
        time.sleep(1)
print ('Tu sens le sol contre toi, il est humide \nMais tu sens aussi que tu es resté fort longtemps dessus...')
time.sleep(1)
conte_a_rebour ()

print ('Tu vois une lumiere')
conte_a_rebour ()

reponse_lever = 'b'
print ('Veux tu te lever ?')
print ('Oui|Non')
reponse_lever= input(str())
if reponse_lever== 'Oui':
    print ('Tu te leves')
else:
    print ('Tu restes au sol')

# while reponse_lever =='Oui':
#     print ('Veux tu te lever ?')
#     print ('Oui|Non')
#     reponse_lever= input(str())
#     if reponse_lever== 'Oui':
#         print ('Tu te leves')
conte_a_rebour ()

print ('Tu te sens fébrile, mais tu arrive a marché jusqu\'au bout de la grotte')
time.sleep(2)

#print ('A tes pieds se trouvent un')
print ('A tes pieds se trouvent un baton')
time.sleep (2)
print ('Veux tu le ramasser?')
baton_ramasser = 'oui'
baton_ramasser = input (str('Oui|Non\n'))
if baton_ramasser== 'Oui':
    print ('Le baton est dans ton inventaire\nPour l\'ouvrir il suffit que tu regardes dans ton sac')
else:
    print ('tu passes ton chemin')

conte_a_rebour ()
print ('Tu vois une pancarte, mais tu n\'arrives pas a lire')
time.sleep (2)
print ('Tu rentres dans la foret')
conte_a_rebour ()
print ('Pour avoir la suite de l\'aventure, achetez le pack d\'extention a 1500$')


