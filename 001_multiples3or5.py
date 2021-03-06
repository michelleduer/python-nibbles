def main():
    """
    Find the sum of all the multiples of 3 or 5 below 1000.
    """
    multi_sum = 0
    for i in range(1000):
        if not i % 3 or not i % 5:
            multi_sum += i
    print(f'\nsum of all multiples of 3 or 5: {multi_sum}')


if __name__ == '__main__':
    main()
