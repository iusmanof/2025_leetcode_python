nums = [-1,2,1,-4]
target = 1
nums.sort()
n = len(nums)
csum = float('inf')

for i in range(n):
    if i > 0 and nums[i] == nums[i-1]:
        print(nums)
        print(nums-1)
        continue
    
    low = i + 1 
    high = n -1
    while low < high:
        current_sum = nums[i] + nums[low] + nums[high]
        
        print("abs csum: ", abs(csum))
        if abs(current_sum - target) < abs(csum - target):
            csum = current_sum
        
        if csum == target:
            # return csum
            print(csum)
        elif csum < target:
            low += 1
        else:
            high -= 1
            
    print(csum)