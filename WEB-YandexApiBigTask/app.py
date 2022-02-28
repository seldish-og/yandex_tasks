from cProfile import run
import pygame
import requests
import sys
import os
import math


class MapInit(object):
    def __init__(self):
        self.lat, self.lon = -33.856951, 151.215137
        self.zoom = 16
        self.type = "map"

    def ll(self):
        return f"{str(self.lon)},{str(self.lat)}"

    def update(self, event):
        my_step = 0.008
        if event.key == 280 and self.zoom < 19:  # Page_UP
            self.zoom += 1
        elif event.key == 281 and self.zoom > 2:  # Page_DOWN
            self.zoom -= 1
        elif event.key == 276:  # LEFT_ARROW
            self.lon -= my_step * math.pow(2, 15 - self.zoom)
        elif event.key == 275:  # RIGHT_ARROW
            self.lon += my_step * math.pow(2, 15 - self.zoom)
        elif event.key == 273 and self.lat < 85:  # UP_ARROW
            self.lat += my_step * math.pow(2, 15 - self.zoom)
        elif event.key == 274 and self.lat > -85:  # DOWN_ARROW
            self.lat -= my_step * math.pow(2, 15 - self.zoom)


def load_map(mp):
    map_url = "http://static-maps.yandex.ru/1.x/?ll={ll}&z={z}&l={type}".format(
        ll=mp.ll(), z=mp.zoom, type=mp.type)
    response = requests.get(map_url)
    print(map_url)
    if not response:
        print("Error")
        print(map_url)

        sys.exit(1)

    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Error with creating file:", ex)
        sys.exit(2)
    return map_file


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    mp = MapInit()
    running = True
    map_file = load_map(mp)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    map_file = pygame.transform.scale(map_file, (10, 10))

        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()

    os.remove(map_file)


if __name__ == "__main__":
    main()
