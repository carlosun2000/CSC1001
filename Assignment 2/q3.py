def obtain_digits():
    while True:
        credit_number = input('Please enter a credit card number (13~16 digits): ')
        if credit_number.isdigit():
                return int(credit_number)    
        else:
            print('not a positive integer')

def isValid(number):
    l = len(str(number))
    if 13 <= l and l <= 16:
        if str(number).startswith('4') or str(number).startswith('5') or str(number).startswith('37') or str(number).startswith('6'):

            sum1 = sumOfDoubleEvenPlace(number)+sumOfOddPlace(number)
            if sum1 % 10 ==0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def sumOfDoubleEvenPlace(number):
    list1 = list(str(number))
    evenList = []
    for i in list1[-2::-2]:
        i = int(i)
        l1 = getDigit(i)
        evenList.append(l1)
    return sum(evenList)



def getDigit(number):
    x = 2*number
    if x < 10:
        digit = x
    else:
        i = x%10
        j = x//10
        digit = i+j
    return digit

def sumOfOddPlace(number):
    list2 = list(str(number))
    sum1 = 0
    for i in list2[-1::-2]:
        i = int(i)
        sum1 += i
    return sum1

number = obtain_digits()
if isValid(number):
    print('It is valid')
else:
    print('It is not valid')
