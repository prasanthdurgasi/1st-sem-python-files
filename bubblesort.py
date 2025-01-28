def bubble_sort(l, n):
    for i in range(n):
        for j in range(n-1-i):
            if l[j] >l[j+1]:
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    print("The sorted Array:")
    print(l)

n = int(input("Enter the number of elements: "))
l = []
for i in range(n):
    l.append(int(input(f"Enter element {i+1}: ")))
print("The original Array:")
print(l)
bubble_sort(l, n)


