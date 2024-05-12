def calculate_experience_points(level):
    total = 0
    for i in range(level):
        total += (i*5)
    return total

def main():
    calculate_experience_points(4)

main()