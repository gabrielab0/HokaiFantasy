#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.entity import Entity



import pygame
from code.entity import Entity
import os

from code.projectile import Projectile


class Player(Entity):

    def __init__(self, name: str, position: tuple, controls: dict):
        super().__init__(name, position)


        # controles
        self.controls = controls

        # velocidade
        self.speed = 5

        # pulo
        self.velocity_y = 0
        self.gravity = 0.8
        self.jump_force = -15
        self.is_jumping = False
        self.shoot_cooldown = 0
        self.shoot_delay = 25
        self.facing_right = True

        PLAYER_ANIMATIONS = {
            "Player1": {
                "idle": ("asset/Player1/idle.png", 8),
                "jump": ("asset/Player1/Jump.png", 10),
                "attack1": ("asset/Player1/attack1.png", 10)
            },

            "Player2": {
                "idle": ("asset/Player2/idle.png", 6),
                "jump": ("asset/Player2/jump.png", 15),
                "attack1": ("asset/Player2/attack1.png",6),
                "attack2": ("asset/Player2/attack2.png", 4),

            }
        }

        data = PLAYER_ANIMATIONS[name]

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
            frame = pygame.transform.scale(frame, (230, 230))
            animation.append(frame)

        return animation

    def move(self):


        projectile = None
        keys = pygame.key.get_pressed()

        # movimento
        if keys[self.controls["right"]]:
            self.rect.x += self.speed

        if keys[self.controls["left"]]:
            self.rect.x -= self.speed

        # pulo
        if keys[self.controls["jump"]] and not self.is_jumping:
            self.velocity_y = self.jump_force
            self.is_jumping = True

        # ataques
        if keys[self.controls["attack1"]]:
            self.state = "attack1"

        if keys[self.controls["attack2"]]:
            self.state = "attack2"

            if self.shoot_cooldown > 0:
                self.shoot_cooldown -= 1

        projectile = None

        shoot_key = self.controls.get("shoot")

        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

        if shoot_key is not None and keys[shoot_key]:

            if self.shoot_cooldown == 0:

                direction = 1 if self.facing_right else -1

                if self.name == "Player1":
                    projectile = Projectile(
                        "FireFox",
                        (self.rect.centerx + 120 * direction, self.rect.centery - 10),
                        direction
                    )

                elif self.name == "Player2":
                    projectile = Projectile(
                        "DarkFire",
                        (self.rect.centerx + 120 * direction, self.rect.centery - 10),
                        direction
                    )

                self.shoot_cooldown = 10

        return projectile

    def update(self):
        # gravidade
        self.velocity_y += self.gravity
        self.rect.y += self.velocity_y
        if self.is_jumping:
            self.state = "jump"

        # chão

        ground = 380

        if self.rect.bottom >= ground:
            self.rect.bottom = ground
            self.velocity_y = 0
            if self.is_jumping:
                self.is_jumping = False
                # só volta para idle se não estiver atacando
                if self.state == "jump":
                    self.state = "idle"

        # animação
        if self.state != self.prev_state:
            self.frame_index = 0
            self.prev_state = self.state

        frames = self.animations.get(self.state, self.animations["idle"])
        pos = self.rect.midbottom
        self.frame_index += self.animation_speed
        if self.frame_index >= len(frames):
            self.frame_index = 0

        self.surf = frames[int(self.frame_index)]
        self.rect = self.surf.get_rect(midbottom=pos)