from tree import CoolTree

t = CoolTree(500, 500)

def setup():
    size(800, 800)
    
def draw():
    global t
    background(0)
    t.update()
    t.draw()
