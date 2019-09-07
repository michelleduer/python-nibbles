from helpers import Helpers


def is_unique(str):
    unique_dict = {}

    if len(str) < 2:
        return True

    for c in str:
        if c in unique_dict:
            print(f'the character {c} is not unique')
            return False
        unique_dict.update({c: 1})
    return True


def main():
    helper = Helpers()
    random_str = helper.create_random_chars_with_choice(11)
    print(f'random str: {random_str}')

    unique = is_unique(random_str)
    if unique:
        print(f'the string is unique')


if __name__ == '__main__':
    main()