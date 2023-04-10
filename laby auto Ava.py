def affiche_laby(laby):
    for i in laby:
        for k in i:
            print(k, end="")
        print()

laby= [[1 for _ in range(8)] for _ in range(6)]
laby[1][1:6] = [0,0,0,0,1]
laby[2][1] = laby[2][5] = 0
laby[3][1:3] = [0,1]
laby[3][5] = 0
laby[4][1:5] = [0,0,1,1]
laby[5][1:7] = [1,0,0,0,0,1]

taille = len(laby)
affiche_laby(laby)
