def merge_sort(l, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(l, left, mid)
        merge_sort(l, mid + 1, right)
        merge(l, left, mid, right)
        
def merge(l, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    Lef = [0] * n1
    Rig = [0] * n2
    
    for i in range(n1):
        Lef[i] = l[left + i]
    
    for j in range(n2):
        Rig[j] = l[mid + 1 + j]
    
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if Lef[i] <= Rig[j]:
            l[k] = Lef[i]
            i += 1
        else:
            l[k] = Rig[j]
            j += 1
        k += 1
    
    while i < n1:
        l[k] = Lef[i]
        i += 1
        k += 1
    
    while j < n2:
        l[k] = Rig[j]
        j += 1
        k += 1

n = int(input("Enter the number of elements: "))
l = []
for i in range(n):
    l.append(int(input(f"Enter element {i + 1}: ")))

print("The original array:")
print(l)

merge_sort(l, 0, n-1)

print("The sorted Array:")
print(l)
