def sum_of_odd_numbers(end):
    total = 0
    for i in range(0, end):
        if not i%2 == 0:
            total += i
    return total
