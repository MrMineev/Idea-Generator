import pygame

class App_Class:
    def __init__(self):
        pygame.init()
        App_Class.screen = pygame.display.set_mode(
            (540, 340)
        )
        App_Class.running = True

    def play(self):
        while App_Class.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    App_Class.running = False

        pygame.quit()

if __name__ == '__main__':
    App_Class().play()
