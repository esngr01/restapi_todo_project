
"""
Spiel "Zahlenraten", in Python programmiert.
"""

import random


print('Zahlenraten')

# initialisiere des Zufallszahlengenerators
random.seed()

number1 = 0
number2 = 0

number_input = 0



# erzeuge neue Zufallszahl zwischen 1 und 100
correct_answer = random.randint(1,100)

player_input = 0
player_input_count = 0

# solange der Spieler noch nicht die richtige Antwort eingegebe hat...
while player_input != correct_answer:
    # lese Eingabe vom Spieler ein und parse den eingegebenen String zu einer Ganzzahl (int)
    player_input = int(input('Zahl eingeben: '))
    # vergleiche Eingabe mit der richtigen Antwort
    if player_input > correct_answer:
        print('Zahl zu groß!')
        player_input_count + 1
    elif player_input < correct_answer:
        print('Zahl zu klein!')
        player_input_count + 1
    else:
        print('Sie haben gewonnen!')
        player_input_count = 0
        
        
# Anzahl der Versuche zählen und am Ende hinter "Sie haben gewonnen!" printen
# Frage Nochmal spielen? am Ende
# Zahlenbereich abfragen (Anpassbar machen?)
# Audio-Datei abspielen wenn gewonnen wurde