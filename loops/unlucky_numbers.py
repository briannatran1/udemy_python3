# loop through number 1-20
    # for 4 and 13, print 'x is unlucky'
    # for even nums, print 'x is even'
    # for odd nums, print 'x is odd'

for x in range (1, 21):
    if x == 4 or x == 13:
        print(f'{x} is unlucky')
    elif x % 2 == 0:
        print(f'{x} is even')
    else:
        print(f'{x} is odd')