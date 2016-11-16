class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    @property
    def data(self):
        return self.data

    @data.setter
    def data(self, data):
        self.data = data

    @property
    def next(self):
        return self.next

    @next.setter
    def next(self, next):
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        new_node = Node(data, None)
        if self.head == None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node

        self.size = self.size + 1

    def delete(self, data):
        current_node = self.head

        while current_node != None:
            if current_node.data == data:
                prev.next = current_node.next
                del current_node
                self.size = self.size - 1
                return

            prev = current_node
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        print current_node.data, "(Head) -> ",
        current_node = current_node.next
        while current_node != None:
            print current_node.data , " -> ",
            current_node = current_node.next
        print "[None]"

    def search(self, data):
        current_node = self.head
        while current_node != None:
            if data == current_node.data:
                return current_node
            current_node = current_node.next

        return None

    def __len__(self):
        return self.size

