# ask for age

# 18 - 20 wristband
# 21+ drink, normal entry
# too young, sorry

# nested statements

age = input('How old are you: ')
if age: # if age isn't empty
    age = int(age)
    if age >= 18 and age <21:
        print('You can enter, but need a wristband!')
    elif age >= 21:
        print('You are good to enter and can drink!')
    else:
        print("You can't come in little one! :(")
else:
    print('Please enter an age!')

# or

age = input('How old are you: ')
if age: # if age isn't empty
    age = int(age)
    if age >= 21:
        print('You are good to enter and can drink!')
    elif age >= 18:
        print('You can enter, but need a wristband!')
    else:
        print("You can't come in little one! :(")
else:
    print('Please enter an age!')