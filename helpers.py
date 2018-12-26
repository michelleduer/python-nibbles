import numpy as np
from random import choices
from string import ascii_lowercase

class Helpers:

    def multiline_print(self, printlist: [int], total_lines: int=1):
        """
        Pretty prints the list to the total number of lines defined
        :param printlist: the list to be printed
        :param total_lines: the total number of lines to print
        """
        length = len(printlist)
        if total_lines < 1:
            return

        step = length // total_lines
        if step < 1:
            return

        for i in range(0, length, step):
            print(f'{printlist[i:i + step]}')

    def create_random_numbers_with_choice(self, upper_limit: int, list_size: int) -> [int]:
        a_range = np.arange(upper_limit)
        return choices(a_range, k=list_size)

    def create_random_chars_with_choice(self, list_size: int):
        return choices(ascii_lowercase, k = list_size)
