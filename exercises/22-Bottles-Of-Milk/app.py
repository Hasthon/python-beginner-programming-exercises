def number_of_bottles():
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

number_of_bottles()