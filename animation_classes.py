from utils.grid import *
import pygame as pg
import sys

# SETTINGS
WIDTH, HEIGHT = 400, 300
RES = (WIDTH, HEIGHT)

class Player():
    def __init__(self, game):
        self.last_update = 0
        self.game = game
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.sprite_sheet = pg.image.load('resources/run.png').convert_alpha()
        self.total_frames = 12
        self.current_frame = 0
        self.frame_rate = 100  # milliseconds

        self.sprite_sheet_width = self.sprite_sheet.get_width() // self.total_frames
        self.sprite_sheet_height = self.sprite_sheet.get_height()


    def draw(self):
        frame_x = (self.current_frame % self.total_frames) * self.sprite_sheet_width
        frame_y = (self.current_frame // self.total_frames) * self.sprite_sheet_height
        image = pg.Surface((self.sprite_sheet_width, self.sprite_sheet_height), pg.SRCALPHA)
        image.blit(self.sprite_sheet, (0, 0), (frame_x, frame_y, self.sprite_sheet_width, self.sprite_sheet_height))
        self.game.screen.blit(image, (self.x, self.y))

    def animate(self):
        now = pg.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % self.total_frames

    def update(self):
        self.animate()


class Game:
    def  __init__(self):
        self.player = None
        pg.init()
        #pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode(RES)
        pg.display.set_caption("First Game With Classes")
        self.new_game()

    '''all game objects inizialization'''
    def new_game(self):
        self.player = Player(self)

    def update(self):
        pg.display.flip()
        self.player.update()

    def draw(self):
        self.screen.fill('white')
        self.player.draw()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    '''combine all Game's calls in one method and run continiosly '''
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
