# -- coding: utf-8 --
# @Time : 2023-02-10 15:01
# @Author : zhangwen
# @File : test.py

# class Person:
#
#
#     def __init__(self,name,gender,age):
#         self.name = name      #实例变量
#         self.gender = gender  #实例变量
#         age = age  #局部变量
#
#     def get_name(self):   #实例方法，必须要实例化
#         return self.name
#
#     def get_age(self):
#         return self.age
#
# xiaoli = Person("小李","Male",18)
#
# print(xiaoli.get_name())   #用实例对象来调用实例方法
#
# from my_page import MyPage
# from my_page import HomePage
# from Common.desired_cap import desired_cap
# from Common.base_page import BasePage
# from headline_page import Headline
# b = HomePage()
# a = MyPage()
# c = BasePage()
# d = Headline()
# a.driver = desired_cap().desired_cap()
# d.driver = a.driver
# a.login_password("13000000000", "abc123456")
# d.publish_video_invitation()
# d.invitation_likes()
# d.invitation_remark()

import pygame
import math

# 初始化Pygame
pygame.init()


# 定义爱心函数
def draw_heart(x, y, size):
    pygame.draw.circle(pygame.Surface([2, 2]), (255, 0, 0), (int(x), int(y)), size)


# 设置画布大小和标题
canvas = pygame.display.set_mode((800, 600))
pygame.display.set_caption("3D Love Heart")

# 绘制爱心
draw_heart(0, 0, 200)

# 循环直到用户关闭窗口
done = False
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

            # 更新画布
    canvas.fill((0, 0, 0))
    draw_heart(0, 0, 200)

    # 绘制文字
    text = pygame.font.SysFont(None, 30).render("Love", True, (255, 255, 255))
    rect = text.get_rect(center=(400, 300))
    canvas.blit(text, rect)

    # 刷新画布
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出Pygame
pygame.quit()