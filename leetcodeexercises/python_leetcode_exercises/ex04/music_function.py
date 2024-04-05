import pygame
def music_play(caminho):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(caminho)
    sound.play()
