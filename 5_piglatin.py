# source of puzzle: http://www.codewars.com/kata/simple-pig-latin/python
# Move the first letter of each word to the end of the word,
# then add "ay" to the end of the word. Leave punctuation marks untouched.
#
# examples:
#   pig_it('Pig latin is cool') # igPay atinlay siay oolcay
#   pig_it('Hello world !')     # elloHay orldway !


def pig_it(phrase):
    add_ay = 'ay'
    pig_latin = ''
    length = len(phrase)
    cursor = 0

    if length < 1:
        return phrase

    for x in range(length):
        # consider spaces and punctuation
        if not phrase[x].isalnum():
            if x != cursor:
                pig_latin = pig_latin + phrase[cursor + 1:x] + phrase[cursor] + add_ay + phrase[x]
            # don't pig latin symbols
            else:
                pig_latin = pig_latin + phrase[x]
            cursor = x + 1

        # consider last word
        elif x == length - 1:
            pig_latin = pig_latin + phrase[cursor + 1:x + 1] + phrase[cursor] + add_ay

    return pig_latin + '\n'


def main():
    test_string = ''
    # empty string
    print('empty string')
    print(pig_it(test_string))

    # single letter
    test_string = 'd'
    print(f'single letter: {test_string}')
    print(pig_it(test_string))

    # word with punctuation
    test_string = 'coffee?'
    print(f'punctuation: {test_string}')
    print(pig_it(test_string))

    # multiple words (deal with spaces)
    test_string = 'happy days'
    print(f'multiple words: {test_string}')
    print(pig_it(test_string))

    # lots of punctuation
    test_string = 'Hi! I am a robot. gibberish 1234!@#$'
    print(f'gibberish: {test_string}')
    print(pig_it(test_string))

    # given test strings
    test_string = 'Pig latin is cool'
    print(f'given string: {test_string}')
    print(pig_it(test_string))

    test_string = 'Hello world !'
    print(f'given string: {test_string}')
    print(pig_it('Hello world !'))


if __name__ == '__main__':
    main()