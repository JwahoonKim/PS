import sys
sys.setrecursionlimit(100000)

a = [1,3,6,2,5,1]

def mergeSort(arr, first, last):
    if(first < last):
        mid = (first + last) // 2
        mergeSort(arr, first, mid)
        mergeSort(arr, mid + 1, last)
        merge(arr, first, mid, last)
    return arr

def merge(arr, first, mid, last):
    tmp = []
    cur1 = first
    cur2 = mid + 1
    while(cur1 <= mid and cur2 <= last):
        if(arr[cur1] < arr[cur2]):
            tmp.append(arr[cur1])
            cur1 += 1
        else:
            tmp.append(arr[cur2])
            cur2 += 1
    while(cur1 <= mid):
        tmp.append(arr[cur1])
        cur1 += 1
    while(cur2 <= last):
        tmp.append(arr[cur2])
        cur2 += 1
    return tmp



mergeSort(a, 0, len(a) - 1)
print(a)