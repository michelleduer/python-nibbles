from helpers import Helpers


def first_duplicate_faster(population: [int]) -> int:
    """
    Faster approach to finding the first duplicated value from the population list.
    e.g. [1, 2, 3, 4, 3, 2, 6, 4] would return the value 3. Uses a dictionary to create
    keys using values. If a key, value pair already exists for a population integer, then
    it is the duplicate.
    :param population: the list of random values
    :return: the duplicate value
    """
    pop_counter = {}
    for p in a:
        if p not in pop_counter:
            pop_counter.update({p: 1})
        else:
            # duplicate found
            return p
    # no duplicates in list
    return -1


def first_duplicate_brute(population: [int]) -> int:
    """
    Brute force approach to finding the first duplicated value from the population list.
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
    helper = Helpers()
    # Create a random list of numbers with replacement
    randlist = helper.create_random_numbers_with_choice(40, 99)

    """
    # (Brute Force) Find the first duplicated value in the list
    first_dup = first_duplicate_brute(randlist)
    if first_dup > -1:
        print(f'\nfirst duplicated value is {first_dup}')
    else:
        print(f'\nno duplicate values')

    """
    print(f'\noriginal list: ')
    helper.multiline_print(randlist, 3)

    # (Faster) Find the first duplicated value in the list
    first_dup = first_duplicate_faster(randlist)
    if first_dup > -1:
        print(f'\nfirst duplicated value is {first_dup}')
    else:
        print(f'\nno duplicate values')

    print(f'\noriginal list: ')
    helper.multiline_print(randlist, 3)


if __name__ == '__main__':
    main()
