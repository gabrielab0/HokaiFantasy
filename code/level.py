#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
from pygame import Font, Surface, Rect

from code.entityMediator import EntityMediator
from code.player import Player
from code.enemy import Enemy
from code.entityFactory import EntityFactory
from code.entity import Entity
from code.projectile import Projectile
from const import C_WHITE, WIN_HEIGHT, MENU_OPTION, C_GREEN, C_CYAN
from const import PLAYER_CONTROLS


class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.running = True
        self.game_mode = game_mode
        self.backgrounds = EntityFactory.get_entity(f'{self.name}Bg')
        self.player_score = player_score


        if self.backgrounds is None:
            self.backgrounds = []

        if self.backgrounds is None:
            self.backgrounds = []

        # lista de entidades
        self.entity_list: list[Entity] = []


        self.clock = pygame.time.Clock()
        self.timeout = 20000

        self.spawn_time = 0
        self.spawn_delay = 5000  # 5 segundos
        self.max_enemies = 3
        self.start_time = pygame.time.get_ticks()

        # controles
        player1_controls = {
            "left": pygame.K_a,
            "right": pygame.K_d,
            "jump": pygame.K_SPACE,
            "attack1": pygame.K_j,
            "attack2": pygame.K_k,
            "shoot": pygame.K_f,
        }

        player2_controls = {
            "left": pygame.K_LEFT,
            "right": pygame.K_RIGHT,
            "jump": pygame.K_UP,
            "attack1": pygame.K_KP1,
            "attack2": pygame.K_KP2,
            "shoot": pygame.K_KP3,
        }

        # modo 1 jogador
        if game_mode == MENU_OPTION[0]:
            player = Player("Player1", (200, 370), player1_controls)
            player.score = player_score[0]

            self.entity_list.append(player)

            self.entity_list.append(
                EntityFactory.get_entity("Enemy", (800, 370))
            )
        # modo 2 jogadores
        elif game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:

            player1 = Player("Player1", (200, 380), player1_controls)
            player1.score = player_score[0]

            player2 = Player("Player2", (350, 380), player2_controls)
            player2.score = player_score[1]

            self.entity_list.append(player1)
            self.entity_list.append(player2)

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

            player = None

            for ent in self.entity_list:
                if isinstance(ent, Player):
                    player = ent
                    break

            # movimento das entidades
            for entity in self.entity_list[:]:
                if isinstance(entity, Player):
                    projectile = entity.move()
                    if projectile:
                        self.entity_list.append(projectile)
                    entity.update()


                elif isinstance(entity, Enemy):

                    entity.update()

                elif isinstance(entity, Projectile):
                    entity.update()
                    if entity.health <= 0:
                        self.entity_list.remove(entity)



            for entity in self.entity_list:
                if isinstance(entity, Player):

                    if entity.name == "Player1":
                        self.level_text(20,
                                        f'Player1 - Health: {entity.health}| Score : {entity.score}',
                                        C_GREEN,
                                        (10, 25)
                                        )

                    elif entity.name == "Player2":
                        self.level_text(20,
                                        f'Player2 - Health: {entity.health} | Score : {entity.score}',
                                        C_CYAN,
                                        (10, 45)
                                        )


            # atualização e desenho
            for entity in self.entity_list:

                if isinstance(entity, Enemy):
                    self.window.blit(entity.get_surf(), entity.rect)
                else:
                    self.window.blit(entity.surf, entity.rect)

            current_time = pygame.time.get_ticks()

            if current_time - self.spawn_time > self.spawn_delay:
                    self.spawn_enemy()
                    self.spawn_time = current_time


            current_time = pygame.time.get_ticks()
            if current_time - self.start_time >= self.timeout:
                return True

            enemies = [e for e in self.entity_list if isinstance(e, Enemy)]
            if len(enemies) == 0 and (current_time - self.start_time) > 3000:

                for ent in self.entity_list:
                    if isinstance(ent, Player) and ent.name == "Player1":
                        self.player_score[0] = ent.score

                    if isinstance(ent, Player) and ent.name == "Player2":
                        self.player_score[1] = ent.score

                return True

            found_player = False
            for ent in self.entity_list:
                if isinstance(ent, Player):
                    found_player = True

            if not found_player:
                return False



            # textos
            time_left = max(0, (self.timeout - (current_time - self.start_time)) / 1000)

            self.level_text(18,
                            f'{self.name} - Time Left: {time_left:.1f}s',
                            C_WHITE,
                            (10, 5)
                            )
            self.level_text(18, f'fps: {self.clock.get_fps():.0f}', C_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(18, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

            # Colissions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
            text_font: Font = pygame.font.SysFont(name=" Lucida sans Typewriter", size=text_size)
            text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
            text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
            self.window.blit(source=text_surf, dest=text_rect)

            self.clock.tick(60)



