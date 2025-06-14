class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def delete_nth_node(self, n):
        if not self.head:
            raise Exception("List is empty")
        if n <= 0:
            raise Exception("Index must be 1 or greater")

        if n == 1:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(n - 2):
            if current.next is None:
                raise Exception("Index out of range")
            current = current.next

        if current.next is None:
            raise Exception("Index out of range")

        current.next = current.next.next
