'''faça um programa em python que aba e reproduza o áudio de um arquivo MP3.'''

import pygame
pygame.init()
pygame.mixer.music.load('flora.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#sou surda então não sei se funcionou :/