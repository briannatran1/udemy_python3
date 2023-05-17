# Use a for loop to add up every odd number from 10 to 20 (inclusive) and store the result in the variable x.

x = 0
for num in range(11, 21, 2):
    x += num
print(x)

# or 

x = 0
for num in range(10, 21):
    if num % 2 != 0:
        x += num
print(x)