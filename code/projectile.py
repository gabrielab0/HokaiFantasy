#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.entity import Entity
import pygame

from code.entity import Entity
import pygame

class Projectile(Entity):

    def __init__(self, name, position, direction):
        super().__init__(name, position)

        self.direction = direction
        self.speed = 2
        self.damage = 1
        self.spawn_protection = 10

        # ===== carregar spritesheet =====
        sheet = self.surf

        self.frames = []
        frame_width = sheet.get_width() // 11
        frame_height = sheet.get_height()

        for i in range(11):
            frame = sheet.subsurface((i * frame_width, 0, frame_width, frame_height))
            self.frames.append(frame)

        # ⭐ escala correta do fogo
        self.frames = [pygame.transform.scale_by(f, 1.4) for f in self.frames]

        self.frame_index = 0
        self.surf = self.frames[0]
        self.rect = self.surf.get_rect(center=position)

        # ⭐ tempo de vida do projétil
        self.life_time = 140

    def move(self):
        self.rect.x += self.speed * self.direction
    def animate(self):
        self.frame_index += 0.35
        if self.frame_index >= len(self.frames):
            self.frame_index = 0

        self.surf = self.frames[int(self.frame_index)]

    def update(self):
        self.move()
        self.animate()

        # ⭐ proteção de spawn correta
        if self.spawn_protection > 0:
            self.spawn_protection -= 1

        self.life_time -= 1
        if self.life_time <= 0:
            self.health = 0

        if self.rect.right < 0 or self.rect.left > pygame.display.get_surface().get_width():
            self.health = 0