#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

import pygame.image


import os

import os

from const import ENTITY_HEALTH


class Entity(ABC):

    def __init__(self, name: str, position: tuple):

        name = name.strip()
        name = name.replace('.png', '')
        name = name.rstrip('.')

        path_character = f'asset/{name}/idle.png'
        path_background = f'asset/{name}.png'

        if os.path.exists(path_character):
            path = path_character
        else:
            path = path_background

        self.surf = pygame.image.load(path).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (738, 432))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.name = name
        self.health = ENTITY_HEALTH[self.name]

    def draw(self, window):
        if self.surf:
            window.blit(self.surf, self.rect)

    @abstractmethod
    def move(self):
        pass







