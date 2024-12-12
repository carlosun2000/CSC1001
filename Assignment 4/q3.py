class Stack:
    def __init__(self):
        self.size = 0
        self.list = list()
    def __len__(self):
        return self.size
    def is_empty(self):
        return self.size == 0
    def push(self,e):
        self.list.append(e)
        self.size += 1
    def top(self):
        if not self.is_empty():
            return self.list[-1]
    def pop(self):
        if not self.is_empty():
            self.size-=1
            return self.list.pop()

def HanoiTower(n):
    A = list(range(1,n+1))[::-1]
    B = Stack()
    C = Stack()
    initial = 'A'
    if n%2 == 1:
        help = 'B'
        goal = 'C'
    else:
        help = 'C'
        goal = 'B'
        
    num = 2**n -1

    for time in range(1,num+1):

        if time % 3 == 1:
            if len(C) == 0 or (len(A) > 0 and A[-1] < C.top()):
                C.push(A.pop())
                print(initial, '-->', goal)
            else:
                A.append(C.pop())
                print(goal, '-->', initial)

        elif time % 3 == 2:
            if len(B) == 0 or (len(A) > 0 and A[-1] < B.top()):
                B.push(A.pop())
                print(initial, '-->', help)
            else:
                A.append(B.pop())
                print(help, '-->', initial)

        else:
            if len(C) == 0 or (len(B) > 0 and B.top() < C.top()):
                C.push(B.pop())
                print(help, '-->', goal)
            else:
                B.push(C.pop())
                print(goal, '-->', help)

if __name__ == '__main__':
    while True: 
        try:    
            n= float(input('please enter an integer: '))
            if n%1==0:
                n=int(n)
                if n>0:
                    break
        except:
            print('invalid input! ')
    HanoiTower(n)
