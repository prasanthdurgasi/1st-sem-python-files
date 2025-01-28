def insertion_sort(l,n):
    for i in range(1,n):
        pivot = l[i]
        j=i-1
        while j >= 0 and l[j] > pivot:
            l[j + 1] = l[j]
            j-=1
        l[j + 1] = pivot
    print("The sorted Array:")
    print(l)

n=int(input("Enter the number of elements:"))
l=[]
for i in range(n):
    l.append(int(input(f"Enter element{i+1}:")))
print("The original array:")
print(l)
insertion_sort(l,n)

