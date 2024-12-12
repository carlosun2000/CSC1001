class terms():
    def __init__(self,variable,order,sign,coefficient):
        self.variable=variable
        self.order = order
        self.coefficient = coefficient
        self.sign = sign
    def one_term_derivative(self):
        self.coefficient = self.coefficient*self.order
        if self.order >0:    
            self.order = self.order - 1
            if self.order ==1:
                return '{}{}*{}'.format(self.sign,self.coefficient,self.variable)
            if self.order == 0:
                return '{}{}'.format(self.sign,self.coefficient)
            else:
                return '{}{}*{}^{}'.format(self.sign,self.coefficient,self.variable,self.order)
        else:
            return ''

class polynomial():
    def __init__(self,variable,polynomial):
        self.variable = variable
        if polynomial.startswith('-'):
            polynomial = polynomial
        else:
            polynomial = '+'+polynomial
        list1 = []
        for i in range(len(polynomial)):
            if polynomial[i] in ["+","-"]:
                list1.append(i)
        list2 = []
        for i in range(len(list1)):
            if i<len(list1)-1:
                s = polynomial[list1[i]:list1[i+1]]
                list2.append(s)
            else:
                list2.append(polynomial[list1[i]:])
        self.terms = list2
        

    def derivatives(self):
        s=''
        for term in self.terms:
            if term.startswith('+'):
                sign = '+'
            else:
                sign = '-'
            term=term.lstrip('-')
            term=term.lstrip('+')
            if not term.isdigit():
                x = term.find('*')
                y = term.find('^')
                if y!=-1 and x==-1:
                    coefficient = 1
                    order = int(term[y+1:])
                if y == -1 and x!=-1:
                    coefficient = eval(term[:x])
                    order = 1
                if y== -1 and x == -1:
                    coefficient = 1
                    order = 1
                if y != -1 and x != -1:
                    coefficient = eval(term[:x])
                    order = int(term[y+1:])

            else:
                order = 0
                coefficient = 0

            one_term = terms(self.variable,order,sign,coefficient)
            s1=one_term.one_term_derivative()
            s1 = s1.rstrip('^0')
            
            s+=s1
        s = s.lstrip('+')
        
        print(s)

while True:            
    poly1 = input('Enter a polynomial: ')
    for i in poly1:
        if not i.isdigit():
            if i not in ['*','^','-','+','.']:
                variable = i
                break

    try:
        poly = polynomial(variable,poly1)
        poly.derivatives()       
        break 
    except:
        print('invalid input')     