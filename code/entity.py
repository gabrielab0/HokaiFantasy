#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import pygame
from abc import ABC, abstractmethod
from const import ENTITY_HEALTH

class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        name = name.strip().replace('.png', '').rstrip('.')
        self.name = name
        self.position = position
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]

        # lista de frames da idle
        self.frames = []
        self.current_frame = 0
        self.animation_speed = 0.15

        # tenta carregar idle_0, idle_1, ...
        path_dir = f'asset/{name}/'
        i = 0
        while os.path.exists(f'{path_dir}idle_{i}.png'):
            self.frames.append(pygame.image.load(f'{path_dir}idle_{i}.png').convert_alpha())
            i += 1

        # se não encontrou múltiplos frames, usa apenas idle.png
        if not self.frames and os.path.exists(f'{path_dir}idle.png'):
            self.frames.append(pygame.image.load(f'{path_dir}idle.png').convert_alpha())

        # fallback: se não tiver nada, mantém o background separado
        if self.frames:
            self.surf = self.frames[0]
            self.rect = self.surf.get_rect(center=position)
        else:
            # se for background, carrega a imagem normal
            path_background = f'asset/{name}.png'
            self.surf = pygame.image.load(path_background).convert_alpha()
            self.rect = self.surf.get_rect(center=position)
            self.frames = [self.surf]

    def update_animation(self):
        """Atualiza apenas a idle"""
        if len(self.frames) > 1:
            self.current_frame += self.animation_speed
            if self.current_frame >= len(self.frames):
                self.current_frame = 0
            self.surf = self.frames[int(self.current_frame)]

    def draw(self, window):
        if self.surf:
            window.blit(self.surf, self.rect)

    @abstractmethod
    def move(self):
        pass






