from helpers import Helpers



def main():
    help = Helpers()
    randlist = help.create_random_chars_with_choice(list_size=99)
    help.multiline_print(randlist, 5)

if __name__ == '__main__':
    main()
