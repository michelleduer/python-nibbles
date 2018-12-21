from helpers import Helpers as help


def fibonacci_recurse(flist: [int], limit: int) -> [int]:
    next_fib = 1
    if not flist:
        return fibonacci_recurse([next_fib], limit)

    length = len(flist)
    if flist[length - 1] < limit:
        if length == 1:
            next_fib = flist[0] + flist[0]
        else:
            next_fib = flist[length - 1] + flist[length - 2]

    if next_fib < limit:
        flist.append(next_fib)
        return fibonacci_recurse(flist, limit)
    return flist


def fibonacci_iter(limit: int) -> [int]:
    flist = [1, 2]
    length = len(flist)

    while flist[length - 1] < limit:
        next_fib = flist[length - 1] + flist[length - 2]
        if next_fib > limit:
            return flist
        flist.append(next_fib)
        length += 1
    return flist
            

def main():
    limit = 1000
    flist = fibonacci_iter(limit)
    print(f'\niterating fibonacci values up to {limit}: ')
    help.pretty_print_list(flist)

    flist = fibonacci_recurse([], limit)
    print(f'\nrecursing fibonacci values up to {limit}: ')
    help.pretty_print_list(flist)


if __name__ == '__main__':
    main()