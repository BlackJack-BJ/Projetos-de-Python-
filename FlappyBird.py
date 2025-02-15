import pygame
from pygame.locals import * #lib with all events

class Birdy: #trying with OOP :P
	def __init__ (self) -> None: #initializing the class
        print()

    def update (self) -> None:
        print()

    def jump (self) -> None:
        self.velocity = -10

    def draw (self) -> None: #to the birdy on the sceeen
       print()


class Pipe:
    def __init__ (self) -> None:
        print()

    def move (self) -> None:
        print()

    def draw (self) -> None:
        print()

    def collision (self) -> None:
        print()


class Game:
    def __init__ (self) -> None:
    def run (self) -> None:
        pygame.init()
        pygame.time.Clock().tick(10)
        while True: #every game is done inside a "while True":
            for event in pygame.event.get():
                if event == pygame.KEYDOWN: #if the event is a KEY
                    bird.jump()

            pygame.display.update() #atualizes the pygame

    def get_events (self) -> int: #the key's data type is INT
        print()

    def update (self) -> None:
        print()

    def draw (self) -> None:
        #Constants
        LENGHT = 600 #x
        WIDTH = 600  #y
        INITIAL_POS_X = LENGHT / 2  #starts in the 
        INITIAL_POS_Y = WIDTH / 2   #middle

        window = pygame.display.set_mode((LENGHT, WIDTH)) #create the window
        window.fill((68, 189, 50))


My_Bird = Birdy()
Your_Pipes = Pipes()
My_Game = Game()
