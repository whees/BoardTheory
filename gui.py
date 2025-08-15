# -*- coding: utf-8 -*-
"""
Created on Thu Aug 14 18:07:29 2025

@author: Luis
"""
import pygame
from librarian import Librarian

class GUI:
    black = (0, 0, 0)
    pink = (255, 0, 255)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    purple = (255, 255, 0)
    orange = (0, 255, 255)
    feet = 0
    start = 1
    middle = 2
    finish = 3
    erase = 4
    colors = {feet: pink, start: green, middle: blue,
              finish: red, erase: purple}
    names = {feet: 'feet', start: 'start',
             middle: 'middle', finish: 'finish', erase: 'erase'}
    
    def __init__(self, size):
        pygame.init()
        self.size = size
        self.surface = pygame.display.set_mode((size,) * 2)
        self.running = True
        self.librarian = Librarian()
        self.wood_img = pygame.transform.scale(pygame.image.load('img/wood.png'), (size, size)).convert_alpha()
        self.plastic_img = pygame.transform.scale(pygame.image.load('img/plastic.png'), (size, size)).convert_alpha()
        self.holds = {}
        self.mode = 1
        self.toggle_hold = False
        pygame.display.set_caption('Beta-Field')

    def project_to_board(self, pos):
        return (round(136 * (pos[0] / self.size - 0.5) / 4) * 4,  round(144 * (1 - pos[1] / self.size) / 4) * 4)

    def project_to_screen(self, pos):
        return (int((pos[0] / 136 + 0.5) * self.size), int((1 - pos[1] / 144) * self.size))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.toggle_hold = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    self.mode = self.erase
                if event.key == pygame.K_p:
                    self.mode = self.feet
                if event.key == pygame.K_s:
                    self.mode = self.start
                if event.key == pygame.K_m:
                    self.mode = self.middle
                if event.key == pygame.K_f:
                    self.mode = self.finish
                if event.key == pygame.K_c:
                    self.holds = {}
                if event.key == pygame.K_RETURN:
                    self.running = False

    def update(self):
        if self.toggle_hold:
            mouse_position = pygame.mouse.get_pos()
            board_position = self.project_to_board(mouse_position)
            hold = self.librarian.holds.get(board_position)

            if hold is not None:
                if self.mode in range(4):
                    self.holds[hold] = self.mode
                else:
                    self.holds.pop(hold, None)

            self.toggle_hold = False

    def display(self):
        self.surface.fill(self.black)
        self.surface.blit(self.wood_img, (0, 0))
        self.surface.blit(self.plastic_img, (0, 0))

        for key, value in self.holds.items():
            board_position = self.librarian.reverse_holds[key]
            screen_position = self.project_to_screen(board_position)
            pygame.draw.circle(self.surface, self.colors[value], screen_position, 20, width=4)

        mouse_position = pygame.mouse.get_pos()
        pygame.draw.circle(self.surface, self.colors[self.mode], mouse_position, 10)
        pygame.display.update()

    def main_loop(self):
        while self.running:
            self.handle_events()
            self.update()
            self.display()
        pygame.quit()
        return self.holds