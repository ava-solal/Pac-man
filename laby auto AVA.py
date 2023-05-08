import random

# Dimensions du labyrinthe
largeur_labyrinthe = 20
hauteur_labyrinthe = 20

# Caractères pour représenter les murs, les chemins et les points
mur = '1'
chemin = '0'

# Fonction pour générer un labyrinthe aléatoire
def generer_labyrinthe():
    labyrinthe = [[mur] * (2 * largeur_labyrinthe + 1) for _ in range(2 * hauteur_labyrinthe + 1)]

    def creuser(x, y):
        labyrinthe[y][x] = chemin

        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 2 * largeur_labyrinthe + 1 and 0 <= ny < 2 * hauteur_labyrinthe + 1 and labyrinthe[ny][nx] == mur:
                labyrinthe[ny - dy // 2][nx - dx // 2] = chemin
                creuser(nx, ny)

    creuser(0, 0)
    return labyrinthe

# Afficher le labyrinthe généré
labyrinthe = generer_labyrinthe()
for ligne in labyrinthe:
    print(' '.join(ligne))


