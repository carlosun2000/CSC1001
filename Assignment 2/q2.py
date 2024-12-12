def isprime(num):
    for i in range(2,num):
        if num%i ==0:
            return False
    else:
        return True

def not_palindromic_and_isprime(num):
    s = str(num)
    l = list(s)
    l.reverse()
    s1 = ''
    for i in l:
        i = str(i)
        s1+=i
    if s1 != s:
        s1 = int(s1)
        if isprime(s1):
            return True
        else:
            return False
    else:
        return False

def operations():
    i=2
    j=1
    list1 = []
    while j <= 100:
        if isprime(i) and not_palindromic_and_isprime(i) :
            list1.append(i)
            j+=1
        i+=1
    return list1

def print_the_list():
    list_prime = operations()
    for i in range(len(list_prime)):
        if (i+1)%10 == 0: 
            print(list_prime[i])
        else:
            print(list_prime[i],end='\t')
print_the_list()