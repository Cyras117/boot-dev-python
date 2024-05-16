def fizzbuzz(start, end):
    for n in range(start,end):        
        if n % 3 == n % 5 == 0:
            print("fizzbuzz")
        elif not (n % 3 == 0 or n % 5 == 0):
            print(n)
        elif n % 3 == 0:
            print("fizz")
        else:
            print("buzz")
# Don't Touch Below This Line


def main():
    test(1, 100)
    test(5, 30)
    test(1, 15)


def test(start, end):
    print("Starting test")
    fizzbuzz(start, end)
    print("======================")


main()
