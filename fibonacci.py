num = 10
n1, n2 = 0, 1
if num == 1:
    print(n1)
else:
        print(n1,n2, end=" ")
        for i in range(2, num):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            print(n3, end=" ")
        