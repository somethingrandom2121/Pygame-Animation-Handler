import pygame as py

class animationState:
    def __init__(self,state,frames,startpos,frameDur,celSiz,image):
        self.state = str(state)
        self.frames = int(frames)
        self.image = image
        self.celSiz = py.Vector2(celSiz)
        self.frameDur = frameDur
        self.startpos = py.Vector2(startpos)

class animation:
    def __init__(self,win):
        self.win     = win
        self.celsiz = py.Vector2(0,0)
        self.disi = 0
        self.ipos = py.Vector2(0,0)
        self.cellw = self.celsiz.x
        self.i = 0
        self.frameDur = 0
        self.frames = 0
        self.states = []

    def addState(self,animationStat):
        self.states.append(animationStat)

    def setState(self,stateName):
        for frame in self.states:
            if frame.state == stateName:
                self.i = 0
                self.disi = 0
                self.celsiz = frame.celSiz
                self.cellw = self.celsiz.x
                self.ipos = frame.startpos
                self.image = frame.image
                self.frames = frame.frames
                self.frameDur = frame.frameDur

    def changeFrame(self):
        self.i += 1
        if self.i == self.frameDur:
            self.disi += 1
            if self.disi == self.frames:
                self.disi = 0
            self.i = 0
    def render(self):
        x = self.cellw*self.disi
        self.win.blit(self.image,self.ipos,(x,0,self.celsiz.x,self.celsiz.y))


#animation states are held in the animation, use addState to add animationstate

#to set an animation state use setState

#to cycle animation use changeFrame

#render animation using render
