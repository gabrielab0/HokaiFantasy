#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Font, Surface, Rect

from code.entityFactory import EntityFactory
from code.entity import Entity
from const import COLOR_WHITE, WIN_HEIGHT


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.running = True
        self.game_mode = game_mode
        self.backgrounds = EntityFactory.get_entity('Level1Bg')
        self.entity_list: list[Entity] = []
        self.clock = pygame.time.Clock()
        self.timeout = 20000

    def run(self):

        pygame.mixer_music.load(f'./asset/{self.name}.wav')
        pygame.mixer_music.play(-1)

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # limpa tela
            self.window.fill((0, 0, 0))

            # backgrounds
            for bg in self.backgrounds:
                bg.move()
                bg.draw(self.window)

            # entidades
            for ent in self.entity_list:
                ent.move()
                ent.draw(self.window)

            # textos
            self.level_text(18, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(18, f'fps: {self.clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(18, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()
        pass


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
            text_font: Font = pygame.font.SysFont(name=" Lucida sans Typewriter", size=text_size)
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
            self.window.blit(source=text_surf, dest=text_rect)

            self.clock.tick(60)