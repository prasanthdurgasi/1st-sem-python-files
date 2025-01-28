def max_of_three(s1, s2, s3):
    if s1 > s2 and s1 > s3:  
        print("The greatest number is:", s1)
    elif s2 > s1 and s2 > s3:  
        print("The greatest number is:", s2)
    else:
        print("The greatest number is:", s3)

max_of_three(10, 20, 2)
