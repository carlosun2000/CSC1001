def generate_the_lockers():
    global list1
    list1 = []
    for _ in range(100):
        list1.append(False)
    
def process():
    for i in range(1,101):
        for j in range(i,101,i):
            list1[j-1] = not(list1[j-1])   

def test():
    generate_the_lockers()
    process()
    list_open=[]
    list_close = []
    for i in range(1,len(list1)+1):
        if list1[i-1] :
            list_open.append(i)
        else:
            list_close.append(i)
    print('open',list_open)

test()      