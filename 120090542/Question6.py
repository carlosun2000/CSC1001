from math import sin
from math import cos
from math import tan

def integral(a,b,n):
        inte = 0
        if function == 'sin':
            for i in range(1,1+n):
                inte += (b-a)/n*sin(a+(b-a)/n*(i-0.5))
        elif function == 'cos':
            for i in range(1,1+n):
                inte += (b-a)/n*cos(a+(b-a)/n*(i-0.5))
        else:
            for i in range(1,1+n):
                inte += (b-a)/n*tan(a+(b-a)/n*(i-0.5))
        return inte

while True:
    func = ['sin','cos','tan']
    function = input('please enter a funtion name (sin,cos,tan): ')
    
    if function in func:
       break
    else:
        print('invalid input')
while True:
    try:
        n=float(input('please enter a number for n: '))
            
        if n%1 ==0 and n>0:
            n=int(n)
            break
        else:
            print('n is not an positive integer')
                
    except:
        print('your input in n is invalid')
while True:
    try:
        a=float(input('please enter a number for a: '))
        b=float(input('please enter a number for b: '))
        if a <= b:
            result = integral(a,b,n)
            print('Result is:',result)
            break
        else:
            print('a must be less than b')
    except:
        print('a,b must be digit')