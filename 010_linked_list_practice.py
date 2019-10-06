from DataStructures import LinkedList


def main():
    a_list = LinkedList()
    a_list.generate_random()
    print('\nnew list: ', end='')
    a_list.display()
    print(f'list size: {a_list.size()}')


if __name__ == '__main__':
    main()
