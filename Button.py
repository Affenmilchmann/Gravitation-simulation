from Physics import DrawText

class Button():
    def __init__(self, pos, size, text, color = (100, 100, 100)):
        self.pos = pos; self.size = size; self.color = color; self.text = text; self.IsActive = False

    def Press(self, P, HardPress = False):
        ans = (P[0] > self.pos[0] and P[1] > self.pos[1] and P[0] < self.pos[0] + self.size[0] and P[1] < self.pos[1] + self.size[1]) or HardPress
        if ans:
            self.IsActive = not self.IsActive
            if self.IsActive:
                self.color = (self.color[0] - 50, self.color[1] + 50, self.color[2] - 50)
            else:
                self.color = (self.color[0] + 50, self.color[1] - 50, self.color[2] + 50)

        return ans

    def Collide(self, P):   
        return (P[0] > self.pos[0] and P[1] > self.pos[1] and P[0] < self.pos[0] + self.size[0] and P[1] < self.pos[1] + self.size[1])

    def DrawText(self, surf):
        DrawText((self.pos[0] + 10, self.pos[1] + 10), 15, surf, (255, 255, 255), self.text)
