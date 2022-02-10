from cProfile import run
import pygame
import requests
import sys
import os


class MapInit(object):
    def __init__(self):
        self.lat, self.lon = -33.856951, 151.215137
        self.zoom = 16
        self.type = "map"

    def ll(self):
        return f"{str(self.lon)},{str(self.lat)}"


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
            elif event.type == pygame.KEYUP:
                mp.update(event)

        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
    pygame.quit()

    os.remove(map_file)


if __name__ == "__main__":
    main()
