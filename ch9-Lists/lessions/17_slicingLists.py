def get_champion_slices(champions):
    return champions[2:],champions[:-2],champions[::2]

def main():
    print(get_champion_slices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

main()
