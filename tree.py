import random

class CoolTree:
    
    def __init__(self, x, y, value = None):
        self.x = x
        self.y = y
        self.value = value
        self.left = None
        self.right = None
    def insert(self, child):
        if self.value > child.value:
            if self.left == None:
                self.left = child
            else:
                self.left.insert(child)
        else:
            if self.right == None:
                self.right = child
            else:
                self.right.insert(child)
        
    def update(self):
        pass      
                        
    def draw(self):
        if self.left is not None:
            stroke(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            fill(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            line(self.x, self.y, self.left.x, self.left.y)
            ellipse(self.x, self.y, 20, 20)
            self.left.draw()
        if self.right is not None:
            stroke(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            fill(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            line(self.x, self.y, self.right.x, self.right.y)
            ellipse(self.x, self.y, 20, 20)
            self.right.draw()        
        
        
