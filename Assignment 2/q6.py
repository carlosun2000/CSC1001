import random
list1 = [' ']*64
def obtain_the_position(i):
    column = i%8+1
    row = i//8+1
    return column,row

def column_list(i):
    column_list = list1[i-1::8]
    return column_list

def row_list(i):
    row_list = list1[8*i-8:8*i]
    return row_list

def position(column,row):
    position= column+row*8-9
    return position


def down_ward_list(i):
    column,row = obtain_the_position(i)
    d_list=[]
    while column>=1 and column<=8 and row>=1 and row<=8:
        p=position(column,row)
        d_list.append(p)
        column+=1
        row+=1
    column,row = obtain_the_position(i)
    while column>=1 and column<=8 and row>=1 and row<=8:
        p=position(column,row)
        column-=1
        row-=1
        d_list.append(p)
    set1 = set(d_list)
    d_list1 = list(set1)
    d_list=[]
    for i in d_list1:
        d_list.append(list1[i])
    return d_list

def up_ward_list(i):
    column,row = obtain_the_position(i)
    d_list=[]
    while column>=1 and column<=8 and row>=1 and row<=8:
        p=position(column,row)
        column-=1
        row+=1
        d_list.append(p)
    column,row = obtain_the_position(i)
    while column>=1 and column<=8 and row>=1 and row<=8:
        p=position(column,row)
        column+=1
        row-=1
        d_list.append(p)
    set1 = set(d_list)
    d_list1 = list(set1)
    d_list=[]
    for i in d_list1:
        d_list.append(list1[i])
    return d_list

def print_list1():
    for i in range(len(list1)):
        if i%8 == 0:
            print('|',end='')
        if (i+1)%8 != 0:
            print(list1[i],'|',sep='',end='')
        else:
            print(list1[i],'|',sep='')


def gene_list():
    global list1
    list1=[' ']*64
    list9 = []

    for i in range(0,8):
        while True:
            ran = random.randint(0,7)
            if ran not in list9:
                list9.append(ran)
                break
        for j in range(0,8):
            if j == ran:
                list1[8*i+j]='Q'

        
def isvalid():
    for i in range(len(list1)):
        d_list1 = up_ward_list(i)
        d_list2 = down_ward_list(i)
        if d_list1.count('Q')>1 or d_list2.count('Q')>1:
            return False     
    else:
        return True

def operation():
    while True:
        gene_list()
        if isvalid():
            print_list1()
            break

operation()