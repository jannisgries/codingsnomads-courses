# Print out every prime number between 1 and 1000.
for number in range(1,1001): # 1, 2, 
    primeNumber = True
    for dividor in range(1, number + 1):
        if dividor != number and dividor != 1:
            if number % dividor == 0:
                primeNumber = False
    if primeNumber:
        print("Number '" + str(number) + "' is a prime number")
