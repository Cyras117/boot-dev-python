def remove_duplicates(spells):
    not_dup_spels=set()
    not_dup_spels_list = []
    for spell in spells:
        not_dup_spels.add(spell)
    for spell in not_dup_spels:
        not_dup_spels_list.append(spell)
    return not_dup_spels_list
