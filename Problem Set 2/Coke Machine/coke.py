coin = int(input('Enter Coin: '))
total = 50
if coin == 10 or coin == 5 or coin == 25:
    a = True
else:
    a = False
while a == True:
    amount = total - coin
    total -= coin
    if total <= 0:
        print('Change Owed:', amount * -1)
        break
    elif amount > 0:
            print('Amount Due:', amount)
    else:
        print('Change Owed:', amount * -1)
    coin = int(input('Enter Coin: '))
if a == False:
    amount = 50
    print('Amount Due:', amount)


    
    