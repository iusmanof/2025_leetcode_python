class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        len_nums = len(nums)
        
        for i in range(len_nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
        
            for j in  range(i+1, len_nums):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                low = j + 1
                high = len_nums - 1
                while low < high:
                    sum = nums[i] + nums[j] + nums[low] + nums[high]
                    if sum == target:
                        result.append([nums[i], nums[j], nums[low], nums[high]])
                        low += 1
                        high -= 1
                        while low < high and nums[low] == nums[low - 1]:
                            low += 1
                        while low < high and nums[high] == nums[high + 1]:
                            high -= 1
                    elif sum < target:
                        low += 1
                    else:
                        high -= 1
                        
        return result
        
        