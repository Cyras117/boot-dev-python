def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    name_max = None
    for enemy in enemies_dict:
        if enemies_dict[enemy] > max_so_far:
            name_max = enemy
            max_so_far = enemies_dict[enemy]
    return name_max