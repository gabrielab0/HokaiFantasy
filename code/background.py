#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity
from const import WIN_WIDTH
from const import ENTITY_SPEED

import pygame

class Background(Entity):

    def __init__(self, name: str):
        super().__init__(name, (0, 0))
        self.scroll = 0
        self.name = name

    def move(self):
        self.scroll -= ENTITY_SPEED[self.name]

        if self.scroll <= -self.rect.width:
            self.scroll += self.rect.width

    def draw(self, window):
        for i in range(3):
            window.blit(self.surf, (self.scroll + i * self.rect.width, 0))