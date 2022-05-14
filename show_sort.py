import time
import pygame


class Show_sort:
    def __init__(self, w, h, show_time):
        pygame.init()
        self.color = [(100, 100, 100), (150, 100, 100), (200, 150, 100), (200, 200, 100),
                      (100, 200, 100), (150, 200, 250), (100, 100, 200), (150, 100, 150)]
        self.window = pygame.display.set_mode((w, h), pygame.RESIZABLE)
        pygame.display.set_caption('Сортировка')
        self.show_time = show_time

    def show(self, array, act=None, wait=False):

        t0 = time.time()
        width, heigth, w, h0, dw = self.get_params(array)

        while time.time() - t0 < self.show_time / len(array) or wait:
            self.window.fill((150, 150, 150))

            for i, e in enumerate(array):
                color = self.color[0] if act is None or i not in act else self.color[1]
                pygame.draw.rect(self.window, color, (25 + i * w, heigth - 100 - h0 * e, w - dw, h0 * e))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                if event.type == pygame.VIDEORESIZE:
                    width, heigth, w, h0, dw = self.get_params(array)

                if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                    return 0

    def get_params(self, array):
        width, heigth = self.window.get_size()
        w = max((width - 50) / len(array), 1)
        h0 = (heigth - 200) / max(array)
        dw = 1 if len(array) < 200 else 0
        return width, heigth, w, h0, dw
