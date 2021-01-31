
def number_of_bottles():
    for i in range(99,-1,-1):
        if i == 1:
            print('1 bottle of milk on the wall, 1 bottle of milk.')
            print('Take one down and pass it around, no more bottles of milk on the wall.')
        elif i == 0:
            print('No more bottles of milk on the wall, no more bottles of milk.')
            print('Go to the store and buy some more, 99 bottles of milk on the wall.')
        else:
            print(str(i)+ ' bottles of milk on the wall, '+str(i)+' bottles of milk.')
            print('Take one down and pass it around, '+str(i-1)+' bottles of milk on the wall.')

number_of_bottles()









""" def number_of_bottles():
    bottles = 99
    while bottles > 1:
        print(str(bottles)+ ' bottles of milk on the wall, '+ str(bottles)+' bottles of milk.')
        bottles -=1
        print('Take one down and pass it around, '+ str(bottles)+' bottles of milk on the wall')
        if bottles == 1:
            print(str(bottles)+' bottle of milk on the wall, '+str(bottles)+' bottle of milk.')
            print('Take one down and pass it around, no more bottles of milk on the wall.')
        elif bottles == 0:
            print('no more bottles of milk on the wall, no more bottles of milk.')

            print('Go to the store and buy some more, 99 bottles of milk on the wall.')

number_of_bottles() """