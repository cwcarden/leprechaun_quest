import pygame
from sys import exit
from pygame import mixer


pygame.init()
screen = pygame.display.set_mode((868,436))
pygame.display.set_caption("Leprechaun Quest")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 60)

background_surface = pygame.image.load('assets/graphics/background.jpg')
text_surface = test_font.render("Leprachaun Quest", False, "Dark Green")

#Fox animation variables
fox_surface = pygame.image.load('assets/graphics/fox.gif').convert_alpha()
fox_x_pos = 200


def intro_music():
    mixer.init()
    mixer.music.load('assets/music/space_theme.mp3')
    mixer.music.set_volume(0.3)
    mixer.music.play()


intro_music()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background_surface, (0,0))
    screen.blit(text_surface, (250, 40))
    screen.blit(fox_surface, (fox_x_pos,310))
    fox_x_pos += 10
    pygame.display.update()
    clock.tick(60)