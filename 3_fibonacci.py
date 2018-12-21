from custom_print import CustomPrint as pr


def fibonacci_iter(limit: int) -> [int]:
    flist = [1]
    flist.append(flist[0] + flist[0])
    
    length = len(flist)
    while flist[length - 1] < limit:
        next_fib = flist[length - 1] + flist[length - 2]
        if next_fib > limit:
            return flist
        flist.append(next_fib)
        length += 1
    return flist
            

def main():
    fibonacci100 = fibonacci_iter(100)
    print(f'fibonacci100: {fibonacci100}')
    pr.pretty_print_list(fibonacci100)
    

if __name__ == '__main__':
    main()