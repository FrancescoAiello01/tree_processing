from tree import CoolTree

bst = CoolTree(400, 50, 25)
bst.insert(CoolTree(350, 80, 12))
bst.insert(CoolTree(300, 110, 8))
bst.insert(CoolTree(380, 110, 13))
bst.insert(CoolTree(450, 80, 60))
bst.insert(CoolTree(420, 110, 58))
bst.insert(CoolTree(500, 110, 72))
bst.insert(CoolTree(250, 140, 1))
bst.insert(CoolTree(330, 140, 9))
bst.insert(CoolTree(360, 140, 12.5))
bst.insert(CoolTree(390, 140, 14))
bst.insert(CoolTree(410, 140, 55))
bst.insert(CoolTree(435, 140, 59))
bst.insert(CoolTree(470, 140, 70))
bst.insert(CoolTree(550, 140, 81))


def setup():
    size(800, 800)
    
def draw():
    global t
    background(0)
    bst.update()
    bst.draw()
