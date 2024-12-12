class Node:
    def __init__(self,element,pointer):
        self.element=element
        self.pointer=pointer

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

    def quick_sort(self,node):
        self.head=node
        if self.size<=1:
            return self
        key = self.head.element
        left = SinglyLinkedList()
        p=self.head
        q=p.pointer
        while q != None:
            if q.element<key:
                t=self.delete(p,q)
                left.insert(t.element)
                q=p.pointer
            else:
                p=q
                q = q.pointer

        t = self.head
        self.delete_head()
        t.poniter = None
        right=SinglyLinkedList()
        m=self.head
        while m != None:
            h=self.delete_head()
            right.insert(h)
            m=m.pointer

        left = left.quick_sort(left.head)
        right = right.quick_sort(right.head)

        left.add_tail(t)
        left.concat(right)
        return left
    
    def output(self):
        p = self.head
        while p != None:
            print(p.element)
            p = p.pointer

    def delete(self,p,q):
        p.pointer = q.pointer
        q.pointer = None
        self.size-=1
        return q
    
    def add_tail(self, node):
        if self.size==0:
            self.head = self.tail = node
        else:
            self.tail.pointer = node
            self.tail = node

    def concat(self, right):
        self.tail.pointer = right.head
        self.tail = right.tail
        self.size+=len(right)

    def delete_head(self):
        if self.size == 0:
            print("The list is empty.")
            return
        else:
            t=self.head.element
            self.head = self.head.pointer
            self.size-=1
            return t


    def __len__(self):
        return self.size


SL = SinglyLinkedList()
node1=SL.insert(3)
node2=SL.insert(14)
node3=SL.insert(5)
node4=SL.insert(2)
node5=SL.insert(4)
node6=SL.insert(7)
node7=SL.insert(6)    
Sll=SL.quick_sort(SL.head)
print('the first node\'s reference: ',Sll.head)
