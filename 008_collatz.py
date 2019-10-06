import yappi


def collatz_sequence_length(starting_value: int) -> int:
    """
    Given solution relies on just calculating the length, which takes out the longer and more
    expensive collatz calculation that requires storing the sequence. Passing the integer parameter
    is cheaper than storing, appending, and passing a list data structure.
    :param starting_value: the integer in the collatz
    :return: returns the length
    """
    if starting_value < 2:
        return 1
    if not starting_value % 2:
        return 1 + collatz_sequence_length(starting_value // 2)
    return 1 + collatz_sequence_length(3 * starting_value + 1)


def sequence_length_dictionary(collatz: [int], stored_lengths: {int: int}) -> int:
    """
    Returns the length of the collatz sequence using dynamic storage
    :param collatz: the collatz sequence to measure
    :param stored_lengths: the dynamic table for storing measured lengths
    :return: returns the length of the collatz sequence
    """
    length = 0
    for c in collatz:
        if c in stored_lengths:
            stored_lengths[collatz[0]] = length + stored_lengths[c]
            return stored_lengths[collatz[0]]
        length += 1
    stored_lengths[collatz[0]] = length
    return length


def calculate_collatz(collatz: [int]) -> [int]:
    """
    Calculate the collatz sequence, returning when the appended value is less than 2
    :param collatz:  the current collatz sequence
    :return: the collatz sequence
    """
    n = collatz[len(collatz) - 1]
    if n < 2:
        return collatz
    if not n % 2:
        collatz.append(n // 2)
        return calculate_collatz(collatz)
    collatz.append(3 * n + 1)
    return calculate_collatz(collatz)


def print_collatz(collatz: [int]) -> None:
    """
    Pretty print the collatz sequence
    :param collatz: the collatz sequence
    """
    length = len(collatz)
    for c in range(length):
        if not c == length - 1:
            print(f'{collatz[c]}', end=' -> ')
        else:
            print(f'{collatz[c]}')


def main():
    stored_lengths = {}
    max_length = (-1, -1)
    max_range = 1000000
    yappi.start()
    for i in range(max_range):
        print(f'i: {i}')
        collatz = calculate_collatz([i])
        length = sequence_length_dictionary(collatz, stored_lengths)
        if length > max_length[0]:
            max_length = (length, i)

    for i in range(max_range):
        print(f'i: {i}')
        length = collatz_sequence_length(i)
        if length > max_length[0]:
            max_length = (length, i)
    yappi.stop()
    print(f'The longest collatz sequence is {max_length[0]} with the starting value {max_length[1]}')


if __name__ == '__main__':
    main()
