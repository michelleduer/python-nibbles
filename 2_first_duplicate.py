import numpy as np
from random import choices


def pretty_print(population: [int], total_lines: int=3):
    """
    Pretty prints the list to the total number of lines defined
    :param population: the list to be printed
    :param total_lines: the total number of lines to print
    """
    length = len(population)

    if total_lines < 1:
        return

    step = length // total_lines
    if step < 1:
        return

    print(f'\nlist of values (pretty printed)')
    for i in range(0, length, step):
        print(f'{population[i:i + step]}')


def first_duplicate(population: [int]) -> int:
    """
    Returns the first duplicated value from the population list.
    e.g. [1, 2, 3, 4, 3, 2, 6, 4] would return the value 3
    :param population: the list of random values
    :return: the duplicate value
    """
    length = len(population)
    for first in range(length):
        for second in range(first + 1, length):
            for third in range(second - 1, first, -1):
                if population[third] == population[second]:
                    return population[third]
            if population[first] == population[second]:
                return population[first]
    return -1


def main():
    # Create a random list of numbers with replacement
    a_range = np.arange(40)
    randlist = choices(a_range, k=99)

    # Find the first duplicated value in the list
    first_dup = first_duplicate(randlist)
    if first_dup > -1:
        print(f'\nfirst duplicated value is {first_dup}')
    else:
        print(f'\nno duplicate values')

    pretty_print(randlist)


if __name__ == '__main__':
    main()
