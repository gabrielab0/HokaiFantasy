#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame
from pygame import Font, Surface, Rect

from const import COLOR_TITLE_GOLDEN, COLOR_SHADOW_GOLDEN, MENU_OPTION, WIN_WIDTH, COLOR_WHITE, COLOR_BLACK

# ===== CONFIGURAÇÃO VISUAL DO MENU =====
WIDTH, HEIGHT = 768, 432

TITLE_COLOR = (COLOR_TITLE_GOLDEN)
SHADOW_COLOR = (COLOR_SHADOW_GOLDEN)

TITLE_Y = 120



class Menu:
    def __init__(self, window):
        self.window = window

        # Fundo
        bg = pygame.image.load('./asset/Menubg.png').convert()
        self.bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

        # Fonte do título
        self.title_font: Font = pygame.font.SysFont(
            "Times New Roman", 52, bold=True

        )
        self.menu_font = pygame.font.SysFont(
            "Times New Roman", 26, bold=True
        )
        self.menu_font = pygame.font.SysFont("Arial", 20)

        # Música (uma vez)
        pygame.mixer.music.load('./asset/SoundMenu.wav')
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
        self.window.blit(self.bg, (0, 0))

        # Sombra do título
        self.draw_text(
            "Hokai Fantasy",
            self.title_font,
            SHADOW_COLOR,
            (WIDTH // 2 + 2, TITLE_Y + 2)



        )
        start_y = 260
        spacing = 30

        for i in range(len(MENU_OPTION)):
            self.draw_text_shadow(
                MENU_OPTION[i],
                self.menu_font,
                COLOR_WHITE,
                COLOR_BLACK,
                (WIN_WIDTH // 2, start_y + spacing * i)
            )
        # Título principal
        self.draw_text(
            "Hokai Fantasy",
            self.title_font,
            TITLE_COLOR,
            (WIDTH // 2, TITLE_Y)
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
