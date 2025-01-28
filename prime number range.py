n=int(input("Enter a number :"))
print ("The Prime Numbers in the range are: ")  
for number in range (2, n + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)  