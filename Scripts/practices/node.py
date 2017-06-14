'''
module Node
'''
class Node:
    """
    Node class
    """
    def __init__(self, initdata):
        '''
        initialize the node with data
        '''
        self.data = initdata
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, newdata):
        self.data = newdata

    def set_next(self, newnext):
        self.next = newnext

def main():
    node = Node(23)
    print("hello world %s" % node.get_data())

if __name__ == "__main__":
    main()
