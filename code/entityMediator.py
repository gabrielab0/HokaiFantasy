from code.enemy import Enemy
from code.entity import Entity
from code.projectile import Projectile


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            test_entity = entity_list[i]
            EntityMediator.__verify_collision_window(test_entity)

        projectiles = [ent for ent in entity_list if isinstance(ent, Projectile)]
        enemies = [ent for ent in entity_list if isinstance(ent, Enemy)]

        for proj in projectiles:
            for enemy in enemies:

                if proj.spawn_protection <= 0 and proj.rect.colliderect(enemy.rect):
                    enemy.health -= proj.damage
                    enemy.hit_timer = 10
                    proj.life_time = 10
                    proj.damage = 0
                    break

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        entity_list[:] = [ent for ent in entity_list if ent.health > 0]
