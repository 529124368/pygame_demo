# 导入所需的模块
from asyncio.windows_events import NULL
from platform import python_revision
import sys
import pygame


class Game:

    # 初始化
    def __init__(self):
        self.size = (1200, 600)
        pygame.init()
        # 设置主屏窗口
        self.screen = pygame.display.set_mode(
            self.size, pygame.RESIZABLE | pygame.HWSURFACE)
        # self.screen.fill((0, 255, 0))
        # 设置icon
        icon = pygame.image.load("assect/img/game.png")
        pygame.display.set_icon(icon)
        # fps
        self.fps = pygame.time.Clock()
        # sptite
        self.sprite = NULL
        # text
        self.text = NULL

    # 画面描画
    def render(self, img, pos):
        self.screen.blit(img, pos)

    # 时间监听
    def eventLoop(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.VIDEORESIZE:
                self.size = (e.w, e.h)
                self.screen = pygame.display.set_mode(
                    self.size, pygame.RESIZABLE | pygame.HWSURFACE)
                self.render(self.text, self.setCenterPos(
                    self.text, (self.size[0]/2, self.size[1]/2)))

    # 设置中心坐标
    def setCenterPos(self, img: pygame.Surface, pos):
        textRect = img.get_rect()
        textRect.center = pos
        return textRect

    # 运行游戏
    def run(self):
        # 设置窗口的标题，即游戏名称
        pygame.display.set_caption('hello world')
        # 引入字体类型
        f = pygame.font.Font('assect/font/DiabloHeavy.ttf', 50)
        # 生成文本信息，第一个参数文本内容；第二个参数，字体是否平滑；
        # 第三个参数，RGB模式的字体颜色；第四个参数，RGB模式字体背景颜色；
        self.text = f.render("C lang is great", True, (255, 0, 0), (0, 0, 0))
        # 将准备好的文本信息，绘制到主屏幕 Screen 上。
        self.render(self.text, self.setCenterPos(
             self.text, (self.size[0]/2, self.size[1]/2)))

        while True:
            # 循环获取事件，监听事件状态
            self.eventLoop()
            pygame.display.flip()  # 更新屏幕内容
            self.fps.tick(60)


# 入口
if __name__ == "__main__":
    Game().run()
