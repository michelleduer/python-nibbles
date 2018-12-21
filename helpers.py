class Helpers:

    def pretty_print_list(printlist: [int], total_lines: int=1):
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
