print('How many kilometers did you cycle today?')
kms = input() # asks user to enter something; returns a str -> need to convert to a number
miles = float(kms)/1.60934
miles = round(miles, 2) # round to 2 decimal places
print(f'Your {kms}km ride is {miles}mi')


# round(thing to round, how many decimals points)