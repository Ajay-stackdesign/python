def merge_sort(arr):
    if len(arr) <=1 :
        return
    
    mid = len(arr) //2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)
    merge_Sorted_list(left,right,arr)

def merge_Sorted_list(a,b,arr):
    lenA = len(a)
    lenB = len(b)

    i = j = k = 0

    while i < lenA and j < lenB:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i +=1
        else:
            arr[k] = b[j]
            j +=1
        k +=1

    while i < lenA :
        arr[k] = a[i]
        i +=1
        k +=1
    while j < lenB :
        arr[k] = b[j]
        j +=1
        k +=1
if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)