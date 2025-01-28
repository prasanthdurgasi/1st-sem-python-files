def selection_sort(l,n):
    for i in range(n-1):
        minIndex=i
        for j in range(i+1,n):
            if l[j]<l[minIndex]:
                minIndex=j;
                
        temp=l[minIndex]
        l[minIndex]=l[i]
        l[i]=temp
    print("The sorted Array:")
    print(l)

n=int(input("Enter the number of elements:"))
l=[]
for i in range(n):
    l.append(int(input(f"Enter element{i+1}:")))
print("The original array:")
print(l)
selection_sort(l,n)
