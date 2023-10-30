import pygame
from AnimationHandler import *

win = pygame.display.set_mode((400,400))

run = True

image = pygame.image.load('example.png')

circleState = animationState('circle',5,(0,0),20,(400,400),image)

exampleAnimation = animation(win)
exampleAnimation.addState(circleState)
exampleAnimation.setState('circle')

while run:
    exampleAnimation.changeFrame()

    win.fill((0,0,0))
    exampleAnimation.render()
    pygame.display.update()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

pygame.quit()
quit()