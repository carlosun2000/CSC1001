def initialdepositamount(finalAccountValue,annualinterestRate,numberOfYears):
    IDA = finalAccountValue/((1+annualinterestRate/100)**numberOfYears)
    print('The initial value is ',IDA)

try:
    finalAccountValue = float(input('Enter the final account value: '))
    annualinterestRate = float(input('Enter the annual interest rate:'))
    numberOfYears = int(input('Enter the number of years: '))
    initialdepositamount(finalAccountValue,annualinterestRate,numberOfYears)
except:
    print('invalid input')

