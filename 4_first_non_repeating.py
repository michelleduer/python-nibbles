from helpers import Helpers


def first_non_repeating(randlist: [str]) -> str:
    


def main():
    help = Helpers()
    randlist = help.create_random_chars_with_choice(list_size=60)
    help.multiline_print(randlist, 3)

    first_unique = first_non_repeating(randlist)
    print(f'the first unique character is {first_unique}')

if __name__ == '__main__':
    main()
