#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity
from const import ENTITY_SPEED, WIN_WIDTH


import pygame
from code.entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.speed = 3
        self.direction = -1

        self.velocity_y = 0
        self.gravity = 0.8
        self.is_jumping = False

        ENEMY_ANIMATIONS = {
            "Enemy": {
                "idle": ("asset/Enemy/idle.png", 6),
                "jump": ("asset/Enemy/jump.png", 15),
                "attack1": ("asset/Enemy/attack1.png", 3),
                "attack2": ("asset/Enemy/attack2.png", 6)
            }
        }

        data = ENEMY_ANIMATIONS[name]

        self.animations = {
            state: self.load_animation(path, frames)
            for state, (path, frames) in data.items()
        }

        self.state = "idle"
        self.prev_state = "idle"

        self.frame_index = 0
        self.animation_speed = 0.2

        self.surf = self.animations["idle"][0]
        self.rect = self.surf.get_rect(midbottom=position)

    def load_animation(self, path, frames):

        sheet = pygame.image.load(path).convert_alpha()

        frame_width = sheet.get_width() // frames
        frame_height = sheet.get_height()

        animation = []

        for i in range(frames):
            frame = sheet.subsurface((i * frame_width, 0, frame_width, frame_height))
            frame = pygame.transform.scale(frame, (200, 200))
            animation.append(frame)

        return animation

    def move(self, player):

        if self.rect.centerx > player.rect.centerx:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

    def update(self):

        # gravidade
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y

        ground = 380

        if self.rect.bottom >= ground:
            self.rect.bottom = ground
            self.velocity_y = 0
            self.is_jumping = False

            if self.state == "jump":
                self.state = "idle"

        # reinicia animação se estado mudou
        if self.state != self.prev_state:
            self.frame_index = 0
            self.prev_state = self.state

        frames = self.animations.get(self.state, self.animations["idle"])

        pos = self.rect.midbottom

        self.frame_index += self.animation_speed

        if self.frame_index >= len(frames):
            self.frame_index = 0

        frame = frames[int(self.frame_index)]

        self.surf = frame

        self.rect = self.surf.get_rect()
        self.rect.midbottom = pos