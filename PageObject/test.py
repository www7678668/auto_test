import random
import sys
import pygame
from pygame.locals import *

pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((800, 600))

# 加载小球图像
ball_image = pygame.image.load("ball.png")

# 游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 绘制游戏界面
    screen.fill((255, 255, 255))
    screen.blit(ball_image, (400, 300))

    # 更新游戏界面
    pygame.display.update()

# 退出Pygame
pygame.quit()