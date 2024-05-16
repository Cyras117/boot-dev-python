def count_enemies(enemy_names):
    count_enemies = {}
    for name in enemy_names:
        if name in count_enemies:
            count_enemies[name] += 1
        else:
            count_enemies[name] = 1
    return count_enemies