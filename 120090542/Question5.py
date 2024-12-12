while True:
    try:
        N = input('Enter a integer >=2: ')
        N = float(N)
        list1 = []
        if N%1==0:
            N = int(N)
            if N%1==0 and N>=2:
                for i in range(2,N+1):
                    j=2
                    while j<i:
                        if i%j == 0 :
                            break
                        else:
                            j+=1
                    else:
                        list1.append(i)
                
                print('The prime numbers smaller than {} include: '.format(N))
                for i in range(1,len(list1)+1):
                    if i%8 !=0 :
                        print(list1[i-1],end='\t')
                    else:
                        print(list1[i-1])
                break
    

            else:
                print('your input is not integer lager than 2')
        else:
            print('your input is not an integer')
    except:
        print('your input is not digit')

   


