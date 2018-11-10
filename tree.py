class CoolTree:
    
    def __init__(self, x = 100, y = 100):
        self.x = x
        self.y = y
        
    def update(self):
        self.x += 2
        
    def draw(self):
        ellipse(self.x, self.y, 100, 100)
        
