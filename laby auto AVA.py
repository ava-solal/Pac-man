import random

# longueur
ROWS = 10
# largeur
COLS = 10

lab = []

for i in range(ROWS*2+1):
    lab.append([])
    for j in range(COLS*2+1):
        if i == 0 or j == 0 or i == ROWS*2 or j == COLS*2:
            #  bord du labyrinthe
            lab[i].append("1")
        elif i % 2 == 0 and j % 2 == 0:
            # intersection
            lab[i].append("0")
        elif i % 2 == 0:
            # ligne horizontale
            if random.random() < 0.5:
                lab[i].append("1")
            else:
                lab[i].append("0")
        elif j % 2 == 0:
            # ligne vertical
            if random.random() < 0.5:
                lab[i].append("1")
            else:
                lab[i].append("0")
        else:
            # open space
            lab[i].append("0")
#direction possible
voisin = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}

def avoir_voisin(row, col):
    neighbors = []
    for direction, (drow, dcol) in voisin.items():
        if 0 <= row + drow < ROWS*2+1 and 0 <= col + dcol < COLS*2+1:
            neighbors.append((row + drow, col + dcol, direction))
    return neighbors



def generer_lab():
    row, col = random.randint(0, ROWS*2-1), random.randint(0, COLS*2-1)
    stack = [(row, col)]

    while stack:
        row, col = stack.pop()
        lab[row][col] = "1"
        neighbors = get_neighbors(row, col)
        random.shuffle(neighbors)
        for nrow, ncol, direction in neighbors:
            if lab[nrow][ncol] == "1":
                continue
            remove_wall(row, col, nrow, ncol)
            stack.append((nrow, ncol))

generer_lab()

for row in lab:
    print("".join(row))


