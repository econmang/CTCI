def findSmallest(arr):
    smallest = min(arr)
    arr.remove(smallest)
    return smallest

def selection_sort(arr):
    new_arr = []
    for _ in range(len(arr)):
        smallest = findSmallest(arr)
        new_arr.append(smallest)
    return new_arr

if __name__ == '__main__':
    arr = [8478,394,3,2,4,4,5954,44,323,75,8457,102]

    new_arr = selection_sort(arr)
    print(new_arr)
