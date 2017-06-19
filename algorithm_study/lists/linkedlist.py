"""
Implimentation of a double single linked list in Python

Friday Feb 24th, 2017

"""

# Node object
class Node(object):


    # bool to signify head node
    def __init__(self, value=None, next=None):
        self.value = value
        self.next_node = next

# List object
class LinkList(object):

    # to eventually store the position of the head node
    headnode = None

    def __init__(self):

        # create head node for base list
        self.headnode = Node()

    def traverse_to_end(self):

        curr_node = self.headnode

        while curr_node.next_node is not None:
            curr_node = curr_node.next_node

        return curr_node

    def traverse_to_2_last(self):

        curr_node = self.headnode

        while curr_node.next_node is not None:
            seccondlast = curr_node
            curr_node = curr_node.next_node

        return seccondlast


    def push(self, value):
        # puts a node at the end of the list

        curr_node = self.traverse_to_end()

        curr_node.next_node = Node(value)

    @staticmethod
    def ins(node, value):

        # inserts a node right after the node you give it
        new_node = Node(value)
        # sets the old node's next as the new node's next
        new_node.next_node = node.next_node
        node.next_node = new_node

    def search(self, value):
        # Searches for the first instance of a value in list

        # start at head
        curr_node = self.headnode

        while curr_node.value != value:

            # iterate through until the end of list
            if curr_node.next_node is not None:
                curr_node = curr_node.next_node

            else:
                # returns none if not in list
                return None

        # returns the current node with the correct value
        return curr_node

    def pop(self):

        # removes the node from the very end
        seccondlast = self.traverse_to_2_last()
        seccondlast.next_node = None

    def out_put(self):
        # prints out the list, one value per line

        # starts at the node after head
        curr_node = self.headnode.next_node

        while curr_node is not None:
            print(curr_node.value)

            curr_node = curr_node.next_node

        return 'end of list '

