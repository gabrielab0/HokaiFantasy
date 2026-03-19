#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame
import math
from pygame import Font, Surface, Rect

from const import C_TITLE_GOLDEN, C_SHADOW_GOLDEN, MENU_OPTION, WIN_WIDTH, C_WHITE, C_BLACK, \
    C_YELLOW, OUTLINE_COLOR, WIN_HEIGHT

# ===== CONFIGURAÇÃO VISUAL DO MENU =====
WIDTH, HEIGHT = 768, 432

TITLE_COLOR = (C_TITLE_GOLDEN)
SHADOW_COLOR = (C_SHADOW_GOLDEN)

TITLE_Y = 120



class Menu:
    def __init__(self, window):
        self.window = window
        self.title_time = 0

        # Fundo
        bg = pygame.image.load('./asset/background1.png').convert_alpha()
        self.bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

        # Fonte do título
        self.title_font: Font = pygame.font.SysFont(
            "Times New Roman", 52, bold=True

        )
        self.menu_font = pygame.font.SysFont(
            "Times New Roman", 26, bold=True
        )
        self.selected_option = 0

        # Música (uma vez)
        pygame.mixer.music.load('./asset/SoundMenu.mp3')
        pygame.mixer.music.play(-1)

    def draw_text_shadow(self, text, font, color, shadow_color, center):
            # sombra
            shadow_surf = font.render(text, True, shadow_color)
            shadow_rect = shadow_surf.get_rect(center=(center[0] + 2, center[1] + 2))
            self.window.blit(shadow_surf, shadow_rect)

            # texto principal
            text_surf = font.render(text, True, color)
            text_rect = text_surf.get_rect(center=center)
            self.window.blit(text_surf, text_rect)

    def draw_text(self, text, font, color, center):
        surf = font.render(text, True, color)
        rect = surf.get_rect(center=center)
        self.window.blit(surf, rect)

    def run(self):

        while True:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_DOWN:
                        self.selected_option = (self.selected_option + 1) % len(MENU_OPTION)

                    if event.key == pygame.K_UP:
                        self.selected_option = (self.selected_option - 1) % len(MENU_OPTION)

                    if event.key == pygame.K_RETURN:
                        pygame.display.flip()
                        pygame.time.delay(50)
                        return MENU_OPTION[self.selected_option]

            # -------- DESENHO --------

            self.window.fill((0, 0, 0))

            self.window.blit(self.bg, (0, 0))

            overlay = pygame.Surface((WIN_WIDTH, WIN_HEIGHT))
            overlay.set_alpha(100)
            overlay.fill((0, 0, 0))
            self.window.blit(overlay, (0, 0))

            self.title_time += 0.005
            offset = math.sin(self.title_time) * 5

            TITLE_Y = 120 + offset


            # contorno
            self.draw_text("Hokai Fantasy", self.title_font, OUTLINE_COLOR, (WIDTH // 2 + 2, TITLE_Y))
            self.draw_text("Hokai Fantasy", self.title_font, OUTLINE_COLOR, (WIDTH // 2 - 2, TITLE_Y))
            self.draw_text("Hokai Fantasy", self.title_font, OUTLINE_COLOR, (WIDTH // 2, TITLE_Y + 2))
            self.draw_text("Hokai Fantasy", self.title_font, OUTLINE_COLOR, (WIDTH // 2, TITLE_Y - 2))

            # título
            self.draw_text("Hokai Fantasy", self.title_font, TITLE_COLOR, (WIDTH // 2, TITLE_Y))

            start_y = 260
            spacing = 35

            for i in range(len(MENU_OPTION)):

                if i == self.selected_option:
                    color = C_YELLOW
                else:
                    color = C_WHITE

                self.draw_text_shadow(
                    MENU_OPTION[i],
                    self.menu_font,
                    color,
                    C_BLACK,
                    (WIN_WIDTH // 2, start_y + spacing * i)
                )

            pygame.display.flip()


    def menu_text(
        self,
        text: str,
        font: Font,
        text_color: tuple,
        text_center_pos: tuple
    ):

        text_surf: Surface = font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)
