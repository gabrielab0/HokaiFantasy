#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.player import Player
from code.enemy import Enemy
from const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):

        match entity_name:

            case 'Level1Bg':
                list_bg = []
                for i in range(8):
                    name = f'Level1Bg{i}'
                    bg = Background(name, (0, 0))
                    list_bg.append(bg)
                return list_bg
            case 'Player1':
                return Player('Player1', position)
            case 'Player2':
                return Player('Player2', position)
            case "Enemy":
                return Enemy("Enemy", position)


