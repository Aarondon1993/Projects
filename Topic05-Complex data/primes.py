# Aaron Donnelly
# Computing the primes.

# My list of comments to TBD
P = []
#Loop through all of the numbers we're checking for primality.
for i in range (2,10000):
    # Assume that i is a prime
    isprime = True
    # Loop through all values from 2 up to but not including 
    for j in range(2,i):
        # See if J divides i
        if i % j ==0:
            #If it doest, its isnt prime to exit the loop
          isprime = False
          break

    # If i is prime then append to P  
    if isprime:
     P.append(i)

print(P)        
