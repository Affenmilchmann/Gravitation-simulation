from Session import Session
IsGame = True

Ses = Session((1000, 600))

#Потеря скорости?
#Ses.AddBody((300, 300), (-1, 0), 5000, (100, 20, 20))
#Ses.AddBody((300, 50), (50, 0), 100, (20, 250, 20))


#Система
Ses.AddBody((300, 300), (0, 0), 5000, (200, 150, 20))
Ses.AddBody((300, 250), (240, 0), 1, (10, 250, 50))
Ses.AddBody((300, 500), (-140, 0), 2, (20, 50, 255))
Ses.AddBody((300, 400), (-200, 0), 2, (200, 50, 30))
Ses.AddBody((300, -150), (45, 0), 0.001, (150, 50, 205))

while IsGame:
    Ses.Tick()
    Ses.Draw()
    Ses.Gravitation()
    Ses.CameraMovement()
    Ses.Menu()
    Ses.EditMode()