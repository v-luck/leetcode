class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                nums.pop(i)
                continue
            i += 1

        print(nums)
        return len(nums)




dog = Solution()
print(dog.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
