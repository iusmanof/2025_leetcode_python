def twosum_func(nums, target):
    hashMap = {}
    if len(nums) == 2:
        return [0, 1]
    for index, item in enumerate(nums):
        hashMap[item] = index
    for index, item in enumerate(nums):
        search = target - item
        if search in hashMap:
            if index != hashMap[search]:
                return [index, hashMap[search]]