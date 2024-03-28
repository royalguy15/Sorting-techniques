class Node:
    def init(self , Data):
        self.data = Data
        self.next = None


class LinkedList:
    def init(self):
        self.head = None

    def append(self , data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node.next
        print (current_node.data, end="->")
    