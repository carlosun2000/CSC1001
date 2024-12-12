while True:
    try:
        N = float(input('Please enter an interger: '))
        if N >0 and N%1==0:
            N=int(N)
            break
        else:
            print('invalid input! enter again')
    except:
        print('Not a digit')

print('m\tm+1\tm**(m+1)')

for m in range(1,1+N):
    print(m,m+1,m**(m+1),sep='\t')