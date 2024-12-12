try:
    
    num = float(input('Enter an positive integer: '))
    if num%1==0 and num>0:
        num=str(int(num))
        for i in num:
            print(i)
    else:
        print('your input is not a positive integer')

    
except:
    print('invalid input')