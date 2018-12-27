from helpers import Helpers
import numpy as np


def multiples(numbers: [int]) -> [int]:
    """
    Multiplies all of the values in the list excepting the value at the current index
    e.g. original numbers = [4, 1, 6] returns the multiples = [6, 24, 4] where the
    first value is the product of 1 * 6 and does not include 4.
    :param numbers: the original list of numbers
    :return: the list of multiplied values
    """
    nonzero_indices = np.flatnonzero(numbers)
    total_numbers = len(numbers)
    total_non_zeros = nonzero_indices.size

    # more than one zero
    if total_numbers - total_non_zeros > 1:
        return np.zeros(total_numbers, dtype=np.int16)

    # if there are no zeros, divide each index from the total product
    if total_numbers == total_non_zeros:
        total_product = np.prod(numbers)
        return (total_product / numbers).astype(int)

    # one zero
    total_product = np.zeros(total_numbers, dtype=np.int16)
    np_numbers = np.asarray(numbers)
    zero_index = np.where(np_numbers == 0)[0][0]
    np_numbers[zero_index] = 1
    multiplied_total = np.prod(np_numbers)
    total_product[zero_index] = multiplied_total
    return total_product


def main():
    helper = Helpers()
    randlist = helper.create_random_numbers_with_choice(6, 9)
    print(f'original list:')
    helper.multiline_print(randlist)

    multiplied_values = multiples(randlist)
    print(f'\nmultiplied values: {multiplied_values}')


if __name__ == '__main__':
    main()
