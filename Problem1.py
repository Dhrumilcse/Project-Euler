#Multiples of 3 and 5 below 1000
sum = 0
for number in range (1,1000):
    if (number % 3 == 0 or number % 5 == 0):
        sum = sum + number
print(sum)
