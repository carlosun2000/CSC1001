try:
    n = float(input('Enter a number: '))

    k=0
    if n>=0:
        while k**2<n:
            k+=1
        print(k)

    else:
        print('Any interger\'s square is larger than {}'.format(int(n)))
except:
    print('invalid input')
    
        