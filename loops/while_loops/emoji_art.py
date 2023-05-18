# print emoji using both a for loop and a while loop

# for loop:

for num in range(1, 11):
    print("\U0001f600" * num) 

# while loop:

num = 1
while num <= 10:
    print("\U0001f600" * num) 
    num += 1

# nested loop:

for x in range(3): # repeats inner loop 3 times
    for num in range(1, 11):
        print("\U0001f600" * num) 