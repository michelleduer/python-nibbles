from helpers import Helpers
import numpy as np


def first_non_repeating(randstr: str) -> str:
    """
    Finds the first unique character in a given string or returns a non-alphabetical underscore
    :param randstr: a random string
    :return: the unique char
    """
    list_counter = 1
    counter = np.zeros(26).astype(int)
    order = np.zeros(26).astype(int)
    for r in s:
        key = ord(r) - 97
        counter[key] += 1
        if not order[key]:
            order[key] = list_counter
        list_counter += 1
    unique = np.where(counter == 1)[0]

    if unique.size > 0:
        ordered_unique = np.take(order, unique)
        min_val = np.argmin(ordered_unique)
        first_unique = unique[min_val]
        return chr(first_unique + 97)
    return '_'


def main():
    helper = Helpers()
    randlist = helper.create_random_chars_with_choice(list_size=20)
    randstr = ''.join(randlist)
    print(f'\nrandstr: {randstr}')

    first_unique = first_non_repeating(randlist)
    print(f'the first unique character is {first_unique}')


if __name__ == '__main__':
    main()
