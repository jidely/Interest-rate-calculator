run = True
    
def interestrate():
    principal = int(input('Your invesment: '))
    rate = int(input('Rate: '))
    time = int(input('Time: '))
    taxrate = int(input('Tax Rate: '))

    grossReturn = principal*(rate/100)*time
    totalamount = principal + grossReturn
    netReturn = principal*(rate/100)*time*(1-taxrate/100)

    print(f'Your total amount: {totalamount}\nGross Return: {grossReturn}\nGross Return After Tax: {netReturn}')

def compoundinsterestrate():
    principal = int(input('Your invesment: '))
    rate = int(input('Rate: '))
    maturity = int(input('Time: '))
    ncompound = int(input('Number of Periods: '))

    amount= (principal*(pow(1+(rate/ncompound),maturity)))/100
    gross = amount-principal
    print(f'Your total amount is {amount}\nGross Return: {gross}')

while run:
    option = int(input('Choose the interest you want to calculate\n1-Interest Rate\n2-Compound Interest Rate\n3-If you want to exit: '))
    if option == 1:
        interestrate()
    elif option == 2:
        compoundinsterestrate()
    elif option == 3:
        run = False
    else:
        print('Please Type Valid Number')


