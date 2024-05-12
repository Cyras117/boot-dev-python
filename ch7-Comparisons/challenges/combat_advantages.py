def combat_evaluation(player_power, enemy_defense):
    return player_power>enemy_defense, player_power<enemy_defense, player_power == enemy_defense
