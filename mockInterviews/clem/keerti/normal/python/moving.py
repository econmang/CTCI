'''
    You are moving to a new apartment. You have one street, imagined as a single line:
    1 1 1 1 1 1 1

    At each block on the line [each index], there is an apartment. Each apartment indicates which of several important locations are available on that block (school, gym, store, etc.).
    You are trying to find the apartment that minimizes the farthest distance you'd have to walk to in order to get to each of the locations you care about.

    Example input:
    Blocks = [
            {
                "gym": false,
                "school": true,
                "store": false,
            },
            {
                "gym": true,
                "school": false,
                "store": false,
            },
            {
                "gym": true,
                "school": true,
                "store": false,
            },
            {
                "gym": false,
                "school": true,
                "store": false,
            },
            {
                "gym": false,
                "school": true,
                "store": true,
            },
    ]

   # used to determine which buildings we care about
   Required = ["gym", "school", "store"]
'''

def find_closest(blocks, idx, req):
    left = idx - 1
    right = idx + 1

    while left >= 0 or right < len(blocks):
        if left >= 0:
            if blocks[left][req] == True:
                return idx - left
            else:
                left -= 1
        if right < len(blocks):
            if blocks[right][req] == True:
                return right - idx
            else:
                right += 1

    return len(blocks)

# Will return an array the length of blocks, where each element will be a max distance to a required building
def get_max_dists(blocks, reqs):
    max_dists = []
    max_avail_dist = len(blocks)

    for i, block in enumerate(blocks):
        dists = [max_avail_dist, max_avail_dist, max_avail_dist]
        for j, req in enumerate(reqs):
            if block[req] == True:
                dists[j] = 0
            else:
                dists[j] = find_closest(blocks, i, req)
        max_dists.append(max(dists))

    return max_dists

if __name__ == '__main__':
    blocks = [
            {
                "gym": False,
                "school": True,
                "store": False,
            },
            {
                "gym": True,
                "school": False,
                "store": False,
            },
            {
                "gym": True,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "school": True,
                "store": False,
            },
            {
                "gym": False,
                "school": True,
                "store": True,
            },
    ]

    reqs = ["gym", "school", "store"]

    print("Blocks Received:", blocks)
    print("Required Buidlings:", reqs, "\n")
    max_dists = get_max_dists(blocks, reqs)
    print("Max Distances to Required Buildings:", max_dists)
    best_apt = max_dists.index(min(max_dists))
    print("Best Apartment is Apartment #" + str(best_apt))
