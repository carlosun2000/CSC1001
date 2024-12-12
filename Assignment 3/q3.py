import random
class ecosystem():
    def __init__(self,number_of_fish,number_of_bear,length):
        self.length = length
        self.number_of_fish = number_of_fish
        self.number_of_bear =number_of_bear

    def obtain_the_initial_river(self): 
        
        river = []
        while True:
            x=random.randint(0,self.length-1)
            if x not in river:
                river.append(x)
            if len(river)==self.length:
                break
        for i in range(self.length):
            if river[i] <self.number_of_fish:
                river[i] = 'F'
        for i in range(self.length):
            if river[i] != 'F':
                if river[i] > self.length-self.number_of_bear-1:
                    river[i] = 'B'
        for i in range(self.length):
            if river[i] not in ['F','B']:
                river[i]='N'
        print('the initial river is       ',river)
        return river

    def B_move(self,river,position,move):
        
        if move == 1:
            if river[position-1]=='F' or river[position-1]=='N':
                river[position-1]='B'
                river[position]='N'
            else:
                if 'N' in river:
                    num = river.count('N')
                    x = random.randint(0,num-1)
                    m=0
                    for i in range(self.length):
                        
                        if river[i]=='N':
                            if m == x:
                                river[i]='B'
                                break
                            m+=1
                                            
        if move == 2:
            if river[position+1]=='F' or river[position+1]=='N':
                river[position+1]='B'
                river[position]='N'
            else:
                if 'N' in river:
                    num = river.count('N')
                    x = random.randint(0,num-1)
                    m=0
                    for i in range(self.length):
                        
                        if river[i]=='N':
                            if m == x:
                                river[i]='B'
                                break
                            m+=1
                        

    def F_move(self,river,position,move):
        
        if move == 1:
            if river[position-1]=='B':
                river[position]='N'
            elif river[position-1]=='N':
                river[position]='N'
                river[position-1]='F'
            else:
                if 'N' in river:
                    num = river.count('N')
                    x = random.randint(0,num-1)
                    m=0
                    for i in range(self.length):
                        
                        if river[i]=='N':
                            if m == x:
                                river[i]='F'
                                break
                            m+=1
             
        if move ==2:    
            if river[position+1]=='B':
                river[position]='N'
            elif river[position+1]=='N':
                river[position]='N'
                river[position+1]='F'
            else:
                if 'N' in river:
                    num = river.count('N')
                    x = random.randint(0,num-1)
                    m=0
                    for i in range(self.length):
                        
                        if river[i]=='N':
                            if m == x:
                                river[i]='F'
                                break
                            m+=1
                        
    def simulation(self,N):
        river = self.obtain_the_initial_river()
        for _ in range(N):
            if 'N' in river:
                list1 = []
                for i in range(self.length):
                    if river[i]!='N':
                        list1.append(i)
                for i in range(self.length):
                    if i in list1:
                        if i != 0 and i !=self.length-1:
                            move = random.randint(0,2)
                            if river[i] == 'B':
                                self.B_move(river,i,move)
                            if river[i] == 'F':
                                self.F_move(river,i,move)
                        
                        if i == 0:
                            move = random.randint(0,1)
                            if move == 1:
                                move =2
                            if river[i] == 'B':
                                self.B_move(river,i,move)
                            if river[i] == 'F':
                                self.F_move(river,i,move)

                        if i ==self.length-1:
                            move = random.randint(0,1)
                            if river[i] == 'B':
                                self.B_move(river,i,move)
                            if river[i] == 'F':
                                self.F_move(river,i,move)
        
            else:
                break
        print('after {} moves, the river is {}'.format(N,river))
            

def obtain_the_length():
    while True:
        try:
            length = int(input('Enter the length of the river: '))
            if length >0:
                return length
        except:
            continue

def obtain_the_bear():
    while True:
        try:
            length = int(input('Enter the number of bear: '))
            if length >0:
                return length
        except:
            continue

def obtain_the_fish():
    while True:
        try:
            length = int(input('Enter the number of fish: '))
            if length >0:
                return length
        except:
            continue

def obtain_the_N():
    while True:
        try:
            length = int(input('Enter the number for N: '))
            if length >0:
                return length
        except:
            continue

def test():
    while True:
        b = obtain_the_bear()
        f = obtain_the_fish()
        l = obtain_the_length()
        if b+f<l:
            return f,b,l
        
f,b,l = test()
N = obtain_the_N()
eco = ecosystem(f,b,l)
eco.simulation(N)
