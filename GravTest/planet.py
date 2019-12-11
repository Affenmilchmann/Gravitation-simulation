from Physics import Dist, DrawText
from math import sqrt
from pygame import draw

class Body():
    def __init__(self, P, V, M, Color):
        self.Pos = P
        self.Vel = V
        self.Mass = M
        self.Acc = (0, 0)
        self.Color = Color
        self.IsSelected = False
        self.R = 10

        self.LineLenght = 400
        self.Line = [self.Pos] * self.LineLenght

    def Move(self, dt):
        self.Vel = (self.Vel[0] + self.Acc[0] * dt, self.Vel[1] + self.Acc[1] * dt)
        self.Pos = (self.Pos[0] + self.Vel[0] * dt, self.Pos[1] + self.Vel[1] * dt)

        #a = Dist(self.Line[self.Line.count - 1], self.Pos)


        if (Dist(self.Line[self.LineLenght - 1], self.Pos) > 7):
            self.Line.remove(self.Line[0])
            self.Line.append(self.Pos)

    def Draw(self, surf, Vel, Lines):
        draw.circle(surf, self.Color, (int(self.Pos[0]), int(self.Pos[1])), self.R)

        if Lines:
            for i in range(1, self.LineLenght):
                draw.line(surf, self.Color, self.Line[i - 1], self.Line[i])        
        if Vel:
            DrawText(self.Pos, 10, surf, (255, 255, 255), str(round(sqrt(self.Vel[0]**2 + self.Vel[1]**2), 2)))

        if self.IsSelected:
            draw.rect(surf, (200, 0, 0), ((self.Pos[0] - self.R - 2, self.Pos[1] - self.R - 2), (self.R * 2 + 4, self.R * 2 + 4)), 1)

    def MoveLine(self, X, Y):
        for i in range(self.LineLenght):
            self.Line[i] = (self.Line[i][0] + X, self.Line[i][1] + Y)

    def SetForce(self, F):
        self.Acc = (F[0] / self.Mass, F[1] / self.Mass) #f / m