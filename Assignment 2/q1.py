def generate_values():
    while True:
        try:
            num = float(input('Please enter a positive value for n: '))
            if  num>0:
                return float(num)
            else:
                print('you should enter a positive number')
        except:
            print('you should enter a positive number')

def guess(n):
    lastguess = 10
    while True:
        nextguess=(lastguess+(n/lastguess))/2
        a = max(nextguess,lastguess)
        b = min(nextguess,lastguess)
        if a-b <0.0001:
            return nextguess
        else:
            lastguess = nextguess
n = generate_values()
print(guess(n))