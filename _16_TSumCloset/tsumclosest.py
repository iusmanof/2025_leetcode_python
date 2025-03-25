class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        closest_sum  = float('inf')

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            low = i + 1 
            high = n -1
            while low < high:
                current_sum = nums[i] + nums[low] + nums[high]
                
                if abs(current_sum - target) < abs(closest_sum  - target):
                    closest_sum = current_sum
                
                if current_sum == target:
                    return current_sum
                elif current_sum < target:
                    low += 1
                else:
                    high -= 1
                    
        return closest_sum
        