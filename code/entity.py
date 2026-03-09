#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

import pygame.image


import os

class Entity(ABC):

    def __init__(self, name: str, position: tuple):

        name = name.strip()
        name = name.replace('.png', '')
        name = name.rstrip('.')

        path = os.path.join('asset', name + '.png')

        self.surf = pygame.image.load(path).convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (738, 432))
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self):
        pass







