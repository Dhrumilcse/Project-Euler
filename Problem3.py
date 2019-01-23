import math
#import logging
#logging.basicConfig(level=logging.DEBUG)

#Get Factors
def getFactors(number):
    factors = []
    for potentialFactor in range (1, int(math.sqrt(number)) + 1):
        if number % potentialFactor == 0:
            factors.append(potentialFactor)
            factors.append(number // potentialFactor)
    return factors
#logging.debug(getFactors(13195))

#If the factor is prime
def isPrime(number):
    return len(getFactors(number)) == 2

#Get the largest Prime factor
allFactors = getFactors(600851475143)
primeFactors = []
for factor in allFactors:
    if isPrime(factor):
        primeFactors.append(factor)
print(max(primeFactors))
