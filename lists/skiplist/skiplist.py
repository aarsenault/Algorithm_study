"""
Implimentation of a skip list in Python

Friday Feb 24th, 2017

"""



# make node class

class Node(object):

    # bool to signify head node
    head = False

    def __init__(self, value, height, prev=None, next=None, bot=None, top=None):
        self.value = value
        self.height = height
        self.prev_node = prev
        self.next_node = next
        self.bottom_node = bot
        self.top_node = top


        # make a function that auto sets the node height.
        # self.height =

        # maybe put this in the list methods.


    def node_height(self):




class list(object):

    maxheight = 0

    def __init__(self):
        # initializes the list

        # create head node for base list
        headnode = Node()

        # create head node for maxheight +1




    def ins_node(self):
        # inserts a node


    def del_node(self):
        # removes a node


    def find_val(self):
        # returns the first val
