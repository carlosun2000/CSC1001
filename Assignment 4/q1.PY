class Node:
    def __init__(self,element,pointer):
        self.element = element
        self.pointer = pointer

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    def insert(self,data):
        new_node=Node(data,None)
        new_node.pointer=self.head
        self.head=new_node
        if self.size==0:
            self.tail=new_node
        self.size += 1
        return new_node
 
    def recursive_count(self,node):
        if node==self.tail.pointer:
            return 0
        else:
            return self.recursive_count(node.pointer)+1
       

SL = SinglyLinkedList()
node1=SL.insert(1)
node2=SL.insert(2)
node3=SL.insert(7)
node4=SL.insert(8)
node5=SL.insert(9)
print('The number of nodes is: ',SL.recursive_count(SL.head))