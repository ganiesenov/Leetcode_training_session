nums = [1,1,2, 3, 4,5,5,6,7,7,7,7,7,0, 10]
class Solution:
    def duplicates(self, nums: list) -> list:
        j = 0
        for i in range(1, len(nums)): 
            if nums[i] != nums[j]: 
                j+=1
                nums[j] = nums[i]
        return j+1, nums[:j]
        
solution = Solution()
print(solution.duplicates(nums))