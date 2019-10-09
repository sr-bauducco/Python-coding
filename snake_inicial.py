8 #importando as bibliotecas
import pygame
from pygame.locals import *
import random

#atualizando posicao da laranja
def comida_aleatoria():
    x=random.randint(0,59)
    y=random.randint(0,59)
    return (x * 10, y * 10)

#posições

RIGHT=0
UP=1
LEFT=2
DOWN=3

pygame.init() #inicializando o modulo
tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Oficina:Desenvolvendo o JOOJ da cobrinha')

cobrinha = [(200,200),(210,200),(220,200)]#tamanho da cobra
skin_cobrinha = pygame.Surface((11,11))#espessura
skin_cobrinha.fill((255,244,233))#cor da cobra
direcao = LEFT

orange_posicao = comida_aleatoria()
orange=pygame.Surface((9,9))
orange.fill((255,127,0))


clock =pygame.time.Clock()


while True:
    clock.tick(10)
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
        if evento.type==KEYDOWN:
            if evento.key == K_UP:
                direcao = UP
            if evento.key== K_RIGHT:
                direcao=RIGHT
            if evento.key == K_DOWN:
                direcao=DOWN
            if evento.key == K_LEFT:
                direcao=LEFT


    for i in range(len(cobrinha )-1,0,-1):
        cobrinha[i]=(cobrinha[i-1][0], cobrinha[i-1][i])
        if direcao == UP:
            cobrinha[0]= (cobrinha[0][0], cobrinha[0][1]-10)

        if direcao == DOWN:
            cobrinha[0] = (cobrinha[0][0], cobrinha[0][1] + 10)

        if direcao == LEFT:
            cobrinha[0] = (cobrinha[0][0] -10, cobrinha[0][1])

        if direcao == RIGHT:
            cobrinha[0] = (cobrinha[0][0] +10, cobrinha[0][1])




        tela.fill((0,0,0))
        tela.blit(orange, orange_posicao)
    for i in cobrinha:
        tela.blit(skin_cobrinha,i)
    pygame.display.update()




