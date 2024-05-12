def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        # don't touch above this line
        if i % 2 != 0:
            odd_numbers.append(i)
    # don't touch below this line

    return odd_numbers

def main():
    r = get_odd_numbers(5)
    print(r)

main()