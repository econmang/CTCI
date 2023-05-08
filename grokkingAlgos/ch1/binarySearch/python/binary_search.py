import random

def binary_search(num_list, item):
    low = 0
    high = len(num_list)-1

    while low <= high:
        guess_idx = high + low // 2
        guess = num_list[guess_idx]
        if guess == item:
            return guess_idx
        elif guess < item:
            low = guess_idx + 1
        else:
            high = guess_idx - 1
    return -1
    
if __name__ == "__main__":
    num_list = []
    item = 0
    for i in range(1000):
        random_num = random.randint(0, 10000000)
        if i == 777:
            item = random_num
        num_list.append(random_num)
    num_list.sort()

    search_idx = binary_search(num_list, item)
    print("Search Index: ")
    print(search_idx)
