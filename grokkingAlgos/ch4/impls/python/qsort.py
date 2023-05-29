def qsort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    middle = [pivot]
    left = []
    right = []
    for i in range(1,len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] == pivot:
            middle.append(arr[i])
        else:
            right.append(arr[i])
    return qsort(left) + middle + qsort(right)

# Quicksort using list comprehension
def qsort_lc(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return qsort_lc(less) + [pivot] + qsort_lc(greater)


if __name__ == "__main__":
    arr = [43,29,349,102,1,23,44,23,21,2333,5,4,44,3,55,43]
    sorted_arr = qsort(arr)
    sorted_arr_lc = qsort_lc(arr)
    print("Original Arr:",arr)
    print("Sorted Arr:",sorted_arr)
    print("Sorted Arr w/ List Comprehension:",sorted_arr_lc)
