from random import randint


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

    def set_next(self, next=None):
        self.next = next

    def get_next(self):
        return self.next


class LinkedList:

    def __init__(self, head=None):
        self.head = head
        self.tail = self.head

    def insert(self, new_value: int):
        temp = Node(new_value)
        temp.set_next(self.head)
        self.head = temp

    def display(self):
        if not self.head:
            return print('No list')

        current = self.head
        print(current.value, end='')
        while current.next:
            current = current.next
            print(f' -> {current.value}', end='')
        print('\n')
        return

    def size(self):
        if not self.head:
            return 0
        current = self.head
        size = 1
        while current.next:
            size += 1
            current = current.next
        return size

    def generate_random(self, size: int = 4):
        min_limit = 1
        max_limit = 99
        if size < 1:
            return
        for i in range(1, size + 1):
            self.insert(randint(min_limit, max_limit))

