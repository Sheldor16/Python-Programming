#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint

# Declaration of variables
money = 1000
continuegame = True

print("Welcome !!!")
print('YOu have', '$', money,'.', 'Good Luck !')

while continuegame:
    print('\n________________________________')
    number = int(input('ON which number do you want to bet ?'))
    while number > 49 or number < 0:
        print('You have to bet a number between 0 and 49')
        number = int(input('On which number do you want to bet ?'))
        
    amount = int(input('How much money do you want to bet on this number ?'))
    while amount > money or amount < 1:
        print('You can not bet that with your current amount of money !!')
        amount = int(input('So, how much money do you want to bet on this number ?'))
    numberoutput = randint(0, 49)
    print('\nThe number is', numberoutput)
    
    if number == numberoutput:
        money += 2*amount
        print('Congratulation !! You Won $', money,)
    else:
        money -= amount
        print(' Sorry but you lost, try again !')
    print('\nYoy now have $', money, 'left')
    
    if money == 0:
        continuegame = False
        print('Sorry ubt you do not have enough money to continue ! \nThe game is now ending')
    
    


# In[ ]:




