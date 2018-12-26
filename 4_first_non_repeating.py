from helpers import Helpers
import numpy as np
from numpy import zeros, where


def first_non_repeating(randlist: [str]) -> str:
    """
    Finds the first unique character in a given list or returns a non-alphabetical underscore
    :param randlist: a given list of random characters
    :return: the unique char
    """
    list_counter = 1
    counter = zeros(26).astype(int)
    order = zeros(26).astype(int)
    for r in randlist:
        key = ord(r) - 97
        counter[key] += 1
        if not order[key]:
            order[key] = list_counter
        list_counter += 1
    unique = where(counter == 1)[0]

    if unique.size > 0:
        ordered_unique = np.take(order, unique)
        min_val = np.argmin(ordered_unique)
        first_unique = unique[min_val]
        return chr(first_unique + 97)
    return '_'


def main():
    helper = Helpers()
    randlist = helper.create_random_chars_with_choice(list_size=20)
    helper.multiline_print(randlist, 1)

    first_unique = first_non_repeating(randlist)
    print(f'the first unique character is {first_unique}')


if __name__ == '__main__':
    main()
