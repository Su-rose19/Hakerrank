from array import *

nm = list(map(int, input().split()))
#print(nm)
arr = []
for i in range(nm[0]):
    arr.append(list(map(int, input().split())))
k = int(input())
sorted_arr = sorted(arr, key= lambda x:x[k])
print(lambda x:x[k])
#print(sorted_arr)
for i in range(nm[0]):
    for j in range(nm[1]):
        print(sorted_arr[i][j],end=" ")
    print()