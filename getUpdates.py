# as ab inital task, data for b days is provided to the intern. Then, K updates are performed on the data, where each update is of the form [l,r]. This indicates that the subaray of data starting at index l adn ending at index r is negated. For examples, if data = [1,2,3,4] and updates = [2,4], then data is [1,-2,-3,-4]. inclusive and 1-based indexing is used. given data and k updates. return the final data array after all the updates have been applied.


# O(N + K) time complexity
def getFinalData(data, updates):
    for update in updates:
        data[update[0]-1:update[1]] = [-x for x in data[update[0]-1:update[1]]]
    return data

# O(N + K) is too slow. Need O(K) time complexity
# instead of updating the value each time. we can count how many times each index is updated.
# then we can use the count to determine the final value of each index.


def getFinalDataO1(data, updates):
    count = [0] * len(data)
    for update in updates:
        count[update[0]-1] += 1
        if update[1] < len(data):
            count[update[1]] -= 1

    for i in range(1, len(data)):
        count[i] += count[i-1]

    for i in range(len(data)):
        if count[i] % 2 != 0:
            data[i] = -data[i]

    return data


print(getFinalDataO1([1, -4, -5, 2], [[2, 4], [1, 2]]))
