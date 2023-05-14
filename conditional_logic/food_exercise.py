'''When you run the prewritten code, food will be randomly assigned.  Your task is to write code that will classify what food is.  

If food is set to either 'apple' or 'grape', your code should print 'fruit'.
If food is set to either 'bacon' or 'steak', your code should print 'meat'
If food is set to either 'dirt' or 'worm' your code should print 'yuck''''

# NO TOUCHING ============================================
from random import choice
food = choice(['apple','grape', 'bacon', 'steak', 'worm', 'dirt'])
# NO TOUCHING =============================================

if food == 'apple' or food == 'grape':
    print('fruit')
elif food == 'bacon' or food == 'steak':
    print('meat')
else:
    print('yuck')