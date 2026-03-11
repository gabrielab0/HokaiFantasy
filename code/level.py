#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Font, Surface, Rect

from code.player import Player
from code.enemy import Enemy
from code.entityFactory import EntityFactory
from code.entity import Entity
from const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.running = True
        self.game_mode = game_mode

        self.backgrounds = EntityFactory.get_entity('Level1Bg')

        # lista de entidades
        self.entity_list: list[Entity] = []

        self.clock = pygame.time.Clock()
        self.timeout = 20000

        self.spawn_time = 0
        self.spawn_delay = 5000  # 5 segundos
        self.max_enemies = 3

        # controles
        player1_controls = {
            "left": pygame.K_a,
            "right": pygame.K_d,
            "jump": pygame.K_SPACE,
            "attack1": pygame.K_j,
            "attack2": pygame.K_k
        }

        player2_controls = {
            "left": pygame.K_LEFT,
            "right": pygame.K_RIGHT,
            "jump": pygame.K_UP,
            "attack1": pygame.K_KP1,
            "attack2": pygame.K_KP2
        }

        # modo 1 jogador
        if game_mode == MENU_OPTION[0]:
            self.entity_list.append(
                Player("Player1", (200, 370), player1_controls)
            )
            self.entity_list.append(
                EntityFactory.get_entity("Enemy", (800, 370))
            )

        # modo 2 jogadores
        elif game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(
                Player("Player1", (200, 200), player1_controls)
            )

            self.entity_list.append(
                Player("Player2", (250, 250), player2_controls)
            )

            self.entity_list.append(
                EntityFactory.get_entity("Enemy", (800, 370))
            )

    def spawn_enemy(self):

            enemies = [e for e in self.entity_list if isinstance(e, Enemy)]

            if len(enemies) < self.max_enemies:
                    enemy = EntityFactory.get_entity("Enemy", (900, 370))
                    self.entity_list.append(enemy)

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

            player = self.entity_list[0]

            # movimento das entidades
            for entity in self.entity_list:

                if isinstance(entity, Enemy):
                    entity.move(player)
                else:
                    entity.move()

            # atualização e desenho
            for entity in self.entity_list:
                entity.update()
                entity.draw(self.window)

            current_time = pygame.time.get_ticks()

            if current_time - self.spawn_time > self.spawn_delay:
                    self.spawn_enemy()
                    self.spawn_time = current_time


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