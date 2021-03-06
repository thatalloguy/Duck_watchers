from cardboard.Logger import *
import pygame
pygame.init()
import os

# Get the current working directory

class Board:
    def __init__(self,width,height,title=None,icon=None,fullscreen=None,fps=None,bg=None):
        self.logger = Logger()
        self.width = width
        self.is_sky = False
        self.height = height
        self.title = title
        self.fps = fps
        self.icon = icon
        self.bg = bg
        self.cwd = os.getcwd()
        self.anlog_keys = {0:0, 1:0, 2:0, 3:0, 4:-1, 5: -1}
        self.fullscreen = fullscreen


        self.entities = []

        self.clock = pygame.time.Clock()
        #Window Creation
        if self.fullscreen != None and self.fullscreen == True:
            #self.screen = pygame.display.set_mode([self.width, self.height], pygame.FULLSCREEN)
            #self.logger.send_info("Creating window in fullscreen")
            currentRez = (pygame.display.Info().current_w, pygame.display.Info().current_h)
            self.screen = pygame.display.set_mode(currentRez, pygame.SCALED)


        elif self.fullscreen == None:
            self.screen = pygame.display.set_mode([self.width, self.height])
            self.logger.send_info("Creating window")

        if self.title != None:
            pygame.display.set_caption(self.title)
            self.logger.send_info("Setting the Title to Custom")

        elif self.title == None:
            self.logger.send_info("Setting the Title to template")
            pygame.display.set_caption("A CardBoard Application")

        if self.icon != None:
            self.icon_image = pygame.image.load(self.icon)
            pygame.display.set_icon(self.icon_image)
            self.logger.send_info("Using Custom Icon")

        elif self.icon == None:
            self.icon_image = pygame.image.load((str(self.cwd) + "/cardboard/images/logo.png"))
            pygame.display.set_icon(self.icon_image)
            self.logger.send_info("Using Template Icon")

        if self.fps == None:
            self.fps = 60

        if self.bg == None:
            self.bg = (0,0,0)

    def update(self):
        #self.clock.tick(self.fps)

        pygame.display.flip()
        pygame.display.update()

    def get_all_entities_in_window(self):
        return self.entities

    def add_entity_to_window(self,entity):
        self.entities.append(entity)

    def loop_init(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: quit()
        self.screen.fill((0,0,0))
    def get_key_state(self,key):
        self.keys = pygame.key.get_pressed()

        if self.keys[key]:
            return True


        self.clock.tick(self.fps)

    def __get_joycon_state(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYAXISMOTION:
                self.anlog_keys[event.axis] = event.value

                if abs(self.anlog_keys[0]) > .4:
                    if self.anlog_keys[0] < -.7:
                        return "LEFT"
                    if self.anlog_keys[0] < .7:
                        return "RIGHT"
                if abs(self.anlog_keys[1]) > .4:
                    if self.anlog_keys[1] < -.7:
                        return "UP"
                    if self.anlog_keys[1] < .7:
                        return "DOWN"

    def get_fps(self):
        return str(self.clock.get_fps())
    def set_font(self,fontstyle):
        if fontstyle == "PIXEL":
            self.font = pygame.font.Font((str(self.cwd) + '/cardboard/fonts/FFFFORWA.TTF'), 32)

    def create_text(self,text,color1,color2):
        return self.font.render(text,True,color1,color2)