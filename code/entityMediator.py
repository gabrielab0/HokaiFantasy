from code.enemy import Enemy
from code.entity import Entity
from code.player import Player
from code.projectile import Projectile
from const import WIN_WIDTH


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0 or ent.rect.left > WIN_WIDTH:
                ent.health = 0

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, Projectile):
            valid_interaction = True
        elif isinstance(ent1, Projectile) and isinstance(ent2, Enemy):
            valid_interaction = True


        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                ent1.rect.left <= ent2.rect.right and
                ent1.rect.bottom >=ent2.rect.top and
                ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent2.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def verify_collision(entity_list: list[Entity]):

        projectiles = [ent for ent in entity_list if isinstance(ent, Projectile)]
        enemies = [ent for ent in entity_list if isinstance(ent, Enemy)]

        for proj in projectiles:
            for enemy in enemies:

                if proj.spawn_protection > 0:
                    continue

                if proj.rect.colliderect(enemy.rect):
                    enemy.health -= proj.damage
                    enemy.hit_timer = 10

                    proj.life_time = 10

                    if proj.spawn_protection <= 0 and proj.rect.colliderect(enemy.rect):
                        enemy.health -= proj.damage
                        enemy.last_dmg = proj.name  # ⭐ NÃO PODE FALTAR
                        enemy.hit_timer = 10

                        proj.health = 0

                    break
        players = [ent for ent in entity_list if isinstance(ent, Player)]
        enemies = [ent for ent in entity_list if isinstance(ent, Enemy)]

        for enemy in enemies:
            for player in players:

                if enemy.rect.colliderect(player.rect):

                    if player.hit_timer <= 0:
                        player.health -= enemy.damage
                        player.hit_timer = 20






    @staticmethod
    def __give_score(enemy: Enemy, entity_list: list[Entity]):
        if enemy.last_dmg == 'Projectile':
            for ent in entity_list:
                if ent.name == 'Player1':
                    ent.score += enemy.score
        elif enemy.last_dmg == 'Projectile':
            for ent in entity_list:
                if ent.name == 'Player2':
                    ent.score += enemy.score

    @staticmethod
    def verify_health(entity_list: list[Entity]):

        dead_entities = [ent for ent in entity_list if ent.health <= 0]

        for ent in dead_entities:

            if isinstance(ent, Enemy):



                # ⭐ GARANTE score mesmo se last_dmg falhar
                if ent.last_dmg == "FireFox":
                    for p in entity_list:
                        if isinstance(p, Player) and p.name == "Player1":
                            p.score += ent.score

                elif ent.last_dmg == "DarkFire":
                    for p in entity_list:
                        if isinstance(p, Player) and p.name == "Player2":
                            p.score += ent.score

            entity_list.remove(ent)




       # def verify_health(entity_list: list[Entity]):
           # entity_list[:] = [ent for ent in entity_list if ent.health > 0]
