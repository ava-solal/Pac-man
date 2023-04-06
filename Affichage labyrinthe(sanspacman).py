import pyxel

lab = [
[1,1,1,1,1,1,1,1],
[1,0,0,0,0,1,0,1],
[1,0,1,1,1,1,0,1],
[1,0,1,0,0,0,0,1],
[1,0,0,0,1,1,0,1],
[1,1,1,1,1,1,1,1]]

def verif_taille(laby):
    for i in range(len(laby)-1):
        a = len(laby[i])
        a1 = len(laby[i+1])
        if a != a1:
            return False, a,i,a1,i+1
    return True


def labyrinthe(laby):
    pyxel.init(len(laby[0]), len(laby),title = "labyrinthe")
    if verif_taille(laby) == True:
        for i in range(len(laby)):
            for j in range(len(laby[i])):
                if laby[i][j] == 1:
                    x = j
                    y = i
                    pyxel.pset(x,y,1)
                elif laby[i][j] == 0:
                    x = j
                    y = i
                    pyxel.pset(x,y,0)
                else:
                    x = j
                    y = i
                    pyxel.pset(x,y,10)
        pyxel.mouse(True)
        return pyxel.show()
    else:
        o = verif_taille(laby), "Il y a une erreur dans la longueur du labyrinthe."
        return o
