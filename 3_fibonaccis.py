from helpers import Helpers as help


def fibonacci_recurse(flist: [int], limit: int) -> [int]:
    """
    Recursively calculates the fibonacci sequence up to the defined limit value (inclusive)
    :param flist: the list of fibonacci numbers
    :param limit: the maximum value for the fibonacci sequence
    :return: the fibonacci list of integers
    """
    next_fib = 1
    if limit < 1:
        return flist

    if not flist:
        return fibonacci_recurse([next_fib], limit)

    length = len(flist)
    if flist[length - 1] <= limit:
        if length == 1:
            next_fib = flist[0] + flist[0]
        else:
            next_fib = flist[length - 1] + flist[length - 2]

    if next_fib <= limit:
        flist.append(next_fib)
        return fibonacci_recurse(flist, limit)
    return flist


def fibonacci_iter(limit: int) -> [int]:
    """
    Iteratively calculates the fibonacci sequence up to the defined limit value (inclusive)
    :param flist: the list of fibonacci numbers
    :param limit: the maximum value for the fibonacci sequence
    :return: the fibonacci list of integers
    """
    flist = [1, 2]
    length = len(flist)

    while flist[length - 1] < limit:
        next_fib = flist[length - 1] + flist[length - 2]
        if next_fib > limit:
            return flist
        flist.append(next_fib)
        length += 1
    return flist


def even_modulo(value: int) -> int:
    """
    Returns a value if it is even
    :param value: the value to check
    :return: the even value or -1 if not even
    """
    if not value % 2:
        return value
    return -1


def fibonacci_even(start_list: [int]) -> [int]:
    """
    Takes an original list of fibonacci numbers and returns only the even values as a list
    :param start_list: the original list of fibonacci numbers
    :return: list of even fibonacci integers
    """
    even_list = []
    evens = map(even_modulo, start_list)
    for e in evens:
        even_list.append(e)
    return list(filter(lambda x: x is not -1, even_list))


def main():
    limit = 5432
    flist = fibonacci_iter(limit)
    print(f'\niterating fibonacci values up to {limit}: ')
    help.multiline_print(flist)

    limit = 1010
    flist = fibonacci_recurse([], limit)
    print(f'\nrecursing fibonacci values up to {limit}: ')
    help.multiline_print(flist)

    limit = 5720992
    start_list = fibonacci_iter(100)
    even_flist = fibonacci_even(start_list)
    flist = fibonacci_recurse(even_flist, limit)
    print(f'\neven fibonacci values up to {limit}: ')
    help.multiline_print(flist, 2)


if __name__ == '__main__':
    main()
