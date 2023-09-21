class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        """
        Prints the values of each node in the Stack
        :return: None
        """
        temp = self.top

        while temp:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        """
        Pushes a new Node with the given value onto the top of the Stack
        :param value: The value of the new Node
        :return: True when the new Node is pushed
        """
        new_node = Node(value)

        if self.height == 0:
            self.top = new_node

        else:
            new_node.next = self.top
            self.top = new_node

        self.height += 1
        return True

    def pop(self):
        """
        Pop the top of the stack (remove it)
        :return: The node that was removed, or None if a Node could not be removed.
        """
        if self.height == 0:
            return None

        remove_node = self.top

        self.top = self.top.next
        remove_node.next = None

        self.height -= 1
        return remove_node