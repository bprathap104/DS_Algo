class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
    def add_head_node(self, newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode
    def add_node(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next == None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
    def printList(self):
        if self.head is None:
            print('This is a empty list')
            exit(0)
        currentNode = self.head
        while True:
            if currentNode.next is None:
                print(currentNode.data)
                break
            print(currentNode.data)
            currentNode=currentNode.next

            
sll = SLinkedList()
firstNode = Node('test1')
secondNode = Node('test2')
thirdNode = Node('test3')
sll.add_node(firstNode)
sll.add_node(secondNode)
sll.add_node(thirdNode)
sll.printList()
print('-----------')
prefirstNode = Node('newfirst')
sll.add_head_node(prefirstNode)
sll.printList()