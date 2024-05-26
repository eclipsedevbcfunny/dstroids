import random
import util

import pygame
pygame.init()

import json
with open("config.json") as jd:
    config = json.load(jd)

win = pygame.display.set_mode((config["width"], config["height"]))
clock = pygame.time.Clock()

shipRect = pygame.rect.Rect(0, config["height"] - 100, 80, 80)

score = 0

lives = 3

aX = random.randint(30, config["width"] - 30)
aY = -40
aSpeed = 500

bX = random.randint(30, config["width"] - 30)
bY = -40

pygame.display.set_caption(config["title"])

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    dt = clock.tick(config["fps"])/1000

    shipRect = pygame.rect.Rect(pygame.mouse.get_pos()[0] - 20, config["height"] - 80, 40, 60)

    aRect = pygame.rect.Rect(aX - 10, aY - 10, 20, 20)
    bRect = pygame.rect.Rect(bX - 10, bY - 10, 20, 20)

    win.fill((0, 0, 0))

    pygame.draw.rect(win, (255, 255, 255), shipRect)

    pygame.draw.circle(win, (255, 0, 0), (aX, aY), 20)

    pygame.draw.circle(win, (0, 0, 255), (bX, bY), 20)

    bY += 350 * dt

    aY += aSpeed * dt
    aSpeed += 0.5
    
    if aY >= config["height"] + 40:
        aX = random.randint(30, config["width"] - 30)
        aY = -40
    
    if bY >= config["height"] + 40:
        bX = random.randint(30, config["width"] - 30)
        bY = -40

    if shipRect.colliderect(aRect):
        lives -= 1
        aX = random.randint(30, config["width"] - 30)
        aY = -40

    if shipRect.colliderect(bRect):
        score += 1
        if score % 5 == 0:
            lives += 1
        bX = random.randint(30, config["width"] - 30)
        bY = -40

    if lives == 0:
        pygame.quit()

    util.draw_text(5, 5, pygame.font.Font("font.ttf", 18), "Score: " + str(score), (255, 255, 255), win)
    util.draw_text(5, 28, pygame.font.Font("font.ttf", 18), "Lives: " + str(lives), (255, 255, 255), win)

    pygame.display.flip()
    
    clock.tick(config["fps"])

pygame.quit()