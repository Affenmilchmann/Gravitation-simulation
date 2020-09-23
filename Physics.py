from math import sqrt, sin, cos, atan2
from pygame import font, Rect

font.init()
G = 700

def Grav(Mas1, Mas2, Pos1, Pos2):
    Force = (0, 0)
    dx = Pos1[0] - Pos2[0]
    dy = Pos1[1] - Pos2[1]
    if dx == 0 and dy == 0:
        F = 0
    F = G * Mas1 * Mas2 / (dx*dx+dy*dy)

    ang = atan2(dy, dx)

    Force = (-F * cos(ang), -F * sin(ang))

    return Force


def Dist(Point1, Point2):
    return sqrt((Point1[0] - Point2[0])**2 + (Point1[1] - Point2[1])**2)

def DrawText(Pos, Size, Surf, Color, Text, Style = 'Comic Sans MS'):
    Font = font.SysFont(Style, Size)
    textsurface = Font.render(Text, False, Color)
    Surf.blit(textsurface, Pos)


def IsInside(D1, D2, P):
    r = Rect(D1, (D2[0] - D1[0], D2[1] - D1[1]))
    return r.collidepoint(P)