import pygame
from planet import Body
from Physics import *
from Button import Button
pygame.init()

GRAY = (150, 150, 150)

class Session():
    def __init__(self, Size):
        self.Size = Size
        self.screen = pygame.display.set_mode(Size)
        self.Planetes = []
        self.IsActive = True
        self.IsHolding = False
        self.MenuClick = False
        self.LeftClickUp = False
        self.RightClickHold = False
        self.RightClickUp = False
        self.ButtList = []

        self.ButtList.append(Button((0, 0), (100, 50), 'Menu', (150, 50, 50))) #MenuButt 0
        self.ButtList.append(Button((0, 50), (100, 50), 'Edit Mode', (150, 50, 50))) #EditButt 1

        self.ButtList.append(Button((0, 100), (100, 50), 'Show Vel', (150, 50, 50))) #VelButt 2
        self.ButtList.append(Button((0, 150), (100, 50), 'Show Lines', (150, 50, 50))) #LineButt 3
       
        self.ButtList.append(Button((100, 50), (100, 50), 'Add', (150, 50, 50))) #NewButt 4
        self.ButtList.append(Button((200, 50), (100, 50), 'Delete', (150, 50, 50))) #DeleteButt 5

        self.CreateStep = 0
        self.CreatePos = (0, 0)
        self.CreateVel = (0, 0)
        self.CreateMas = ""
        self.CreateDel = False; self.Enter = False;
        self.Create0 = False; self.Create1 = False; self.Create2 = False; self.Create3 = False; self.Create4 = False; 
        self.Create5 = False; self.Create6 = False; self.Create7 = False; self.Create8 = False; self.Create9 = False; 

        self.IsMenuOpened = False
        self.PrevTime = 0
        self.PlanKol = 0
        self.IsRunning = True
        self.ClickPos = (0, 0)
        self.RClickPos = (0, 0)


        self.FPStick = 0
        self.FPS = 0

    def AddBody(self, Pos, Vel, Mas, Color):
        self.Planetes.append(Body(Pos, Vel, Mas, Color))
        self.PlanKol += 1

    def Tick(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.IsActive = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    self.ClickPos = pygame.mouse.get_pos()
                    self.IsHolding = True
                elif event.button == pygame.BUTTON_RIGHT:
                    self.RightClickHold = True
                    self.RClickPos = pygame.mouse.get_pos()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == pygame.BUTTON_LEFT:
                    self.IsHolding = False
                    self.MenuClick = True
                    self.LeftClickUp = True
                elif event.button == pygame.BUTTON_RIGHT:
                    self.RightClickHold = False
                    self.RightClickUp = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.CreateDel = True 
                elif event.key == pygame.K_0:
                    self.Create0 = True
                elif event.key == pygame.K_1:
                    self.Create1 = True
                elif event.key == pygame.K_2:
                    self.Create2 = True
                elif event.key == pygame.K_3:
                    self.Create3 = True
                elif event.key == pygame.K_4:
                    self.Create4 = True
                elif event.key == pygame.K_5:
                    self.Create5 = True
                elif event.key == pygame.K_6:
                    self.Create6 = True
                elif event.key == pygame.K_7:
                    self.Create7 = True
                elif event.key == pygame.K_8:
                    self.Create8 = True
                elif event.key == pygame.K_9:
                    self.Create9 = True
                elif event.key == pygame.K_SPACE:
                    self.Enter = True

                elif event.key == pygame.K_DOWN:
                    self.Down = True
                elif event.key == pygame.K_UP:
                    self.Up = True
                elif event.key == pygame.K_RIGHT:
                    self.Right = True
                elif event.key == pygame.K_LEFT:
                    self.Left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.Down = False
                elif event.key == pygame.K_UP:
                    self.Up = False
                elif event.key == pygame.K_RIGHT:
                    self.Right = False
                elif event.key == pygame.K_LEFT:
                    self.Left = False
                    
        return self.IsActive


    def Draw(self):
        self.screen.fill((10, 0, 50))

        #Objects with lines Draw
        for B in self.Planetes:
            B.Draw(self.screen, self.ButtList[2].IsActive, self.ButtList[3].IsActive)

        #Selection
        if self.RightClickHold:
            T = pygame.mouse.get_pos()
            x = T[0]; y = T[1]
            pygame.draw.rect(self.screen, (255, 0, 0), (self.RClickPos, (x - self.RClickPos[0], y - self.RClickPos[1])), 1)

        #Menu Draw
        pygame.draw.rect(self.screen, self.ButtList[0].color, (self.ButtList[0].pos, self.ButtList[0].size))
        self.ButtList[0].DrawText(self.screen)
        if self.ButtList[0].IsActive:
            for i in range(1, 4): #Draw Edit Vel and Line butts
                pygame.draw.rect(self.screen, self.ButtList[i].color, (self.ButtList[i].pos, self.ButtList[i].size))
                self.ButtList[i].DrawText(self.screen)

            if self.ButtList[1].IsActive:
                for i in range(4, 6): #Draw Add and Delete butts
                    pygame.draw.rect(self.screen, self.ButtList[i].color, (self.ButtList[i].pos, self.ButtList[i].size))
                    self.ButtList[i].DrawText(self.screen)

        #Create draw
        if self.CreateStep == 1:
            DrawText(self.CreatePos, 20, self.screen, (200, 200, 200), self.CreateMas)

        #################################     
        DrawText((900, 50), 20, self.screen, (200, 200, 200), str(int(self.FPS)))
        self.FPStick += 1
        if self.FPStick > 100:
            self.FPStick = 0
            self.FPS = 1000 / (pygame.time.get_ticks() - self.PrevTime)
        #################################
        pygame.display.flip()

    def Gravitation(self):

        if self.ButtList[1].IsActive:
            return
        
        dt = pygame.time.get_ticks() - self.PrevTime
        self.PrevTime += dt

        if dt > 50: dt = 10
        dt /= 3000

        for i in self.Planetes:
            Force = (0, 0)
            for j in self.Planetes:
                if i != j:
                    F = Grav(i.Mass, j.Mass,  i.Pos, j.Pos)
                    Force = (Force[0] + F[0], Force[1] + F[1])
            i.SetForce(Force)
            i.Move(dt)

    def CameraMovement(self):
        Delta = (0, 0)
        if self.IsHolding:
            M = pygame.mouse.get_pos()
            Delta = (M[0] - self.ClickPos[0], M[1] - self.ClickPos[1])
            for B in self.Planetes:
                B.Pos = (B.Pos[0] + Delta[0], B.Pos[1] + Delta[1])
                B.MoveLine(Delta[0], Delta[1])
            self.ClickPos = M
        self.CamX = 0; self.CamY = 0

    def Menu(self):
        if self.MenuClick:
            self.MenuClick = False
            P = pygame.mouse.get_pos()
            self.ButtList[0].Press(P)
            if self.ButtList[0].IsActive:
                self.ButtList[1].Press(P)
                self.ButtList[2].Press(P)
                self.ButtList[3].Press(P)
                if self.ButtList[1].IsActive:
                    if not self.ButtList[4].IsActive: 
                        self.ButtList[5].Press(P)
                    self.ButtList[4].Press(P)

    def EditMode(self):
        if self.RightClickUp:
            self.RightClickUp = False
            for B in self.Planetes:
                B.IsSelected = IsInside(self.RClickPos, pygame.mouse.get_pos(), B.Pos)     
                self.PlanKol -= 1

        if not self.ButtList[1].IsActive:
            return

        #Delete body
        if self.ButtList[5].IsActive:
            self.ButtList[5].Press((0, 0), True)
            for B in self.Planetes:
                if B.IsSelected:
                    self.Planetes.remove(B)


        #Create new body
        if self.ButtList[4].IsActive:
            if self.CreateStep == 0:
                if self.LeftClickUp:
                    self.LeftClickUp = False                
                    self.CreatePos = pygame.mouse.get_pos()

                    TrueFalse = True
                    for B in self.ButtList:
                        if B.Collide(self.CreatePos): TrueFalse = False

                    if TrueFalse:
                        self.CreateStep += 1

            if self.CreateStep == 1:
                if self.CreateDel:
                    self.CreateDel = False
                    self.CreateMas = self.CreateMas[:-1]
                if self.Create0:
                    self.Create0 = False
                    self.CreateMas += "0"
                if self.Create1:
                    self.Create1 = False
                    self.CreateMas += "1"
                if self.Create2:
                    self.Create2 = False
                    self.CreateMas += "2"
                if self.Create3:
                    self.Create3 = False
                    self.CreateMas += "3"
                if self.Create4:
                    self.Create4 = False
                    self.CreateMas += "4"
                if self.Create5:
                    self.Create5 = False
                    self.CreateMas += "5"
                if self.Create6:
                    self.Create6 = False
                    self.CreateMas += "6"
                if self.Create7:
                    self.Create7 = False
                    self.CreateMas += "7"
                if self.Create8:
                    self.Create8 = False
                    self.CreateMas += "8"
                if self.Create9:
                    self.Create9 = False
                    self.CreateMas += "9"
                if self.Enter:
                    self.Enter = False;
                    self.CreateStep += 1
            if self.CreateStep == 2:
                self.Planetes.append(Body(self.CreatePos, self.CreateVel, int(self.CreateMas), (100, 100, 100)))
                self.PlanKol += 1
                self.CreateStep = 0
