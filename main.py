import pygame

def main():
#    pygame.mixer.init()
#    pygame.mixer.music.load('chocolate.mp3')
#    pygame.mixer.music.play(1)
#    print('ctrl+c stop')
#
#    while True:
#        pass
#    pygame.mixer.music.stop()
    pygame.init()
    pygame.display.set_mode((200,100))
    pygame.mixer.music.load('chocolate.mp3')
    pygame.mixer.music.play(0)

    clock = pygame.time.Clock()
    clock.tick(10)
    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
    

if __name__ == '__main__':
    main()
