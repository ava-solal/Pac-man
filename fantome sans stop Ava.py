import random

# Coordonnées initiales du fantôme
position_x = 0
position_y = 0

# Déplacement aléatoire du fantôme
def deplacement_fantome():
    global position_x, position_y

    # Déterminer un mouvement aléatoire (gauche, droite, haut, bas)
    deplacement = random.choice(['gauche', 'droite', 'haut', 'bas'])

    # Mettre à jour les coordonnées du fantôme en fonction du mouvement
    if deplacement == 'gauche':
        position_x -= 1
    elif deplacement == 'droite':
        position_x += 1
    elif deplacement == 'haut':
        position_y -= 1
    elif deplacement == 'bas':
        position_y += 1

    # Faire en sorte que les coordonnées ne soient jamais négatives
    if position_x < 0:
        position_x += 1

    if position_y < 0:
        position_y += 1


# Boucle continue de déplacement du fantôme
while True:
    # Déplacement du fantôme
    deplacement_fantome()
    print("coordonnées du fantôme : (", position_x, ",", position_y, ")")


