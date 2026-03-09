#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from const import WIN_WIDTH


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):

        match entity_name:

            case 'Level1Bg':
                list_bg = []

                for i in range(8):
                    name = f'Level1Bg{i}'
                    bg = Background(name)
                    list_bg.append(bg)

                return list_bg


