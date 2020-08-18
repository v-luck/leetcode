class Solution(object):
    def twoSum(self, nums, target):
        #this list is used for the final return product
        list = []

        #loop through all numbers in list to run check statement
        for index, value in enumerate(nums):
            second_value = target - value
            #checks for difference value
            if second_value in nums:
                #checks if the indexes are the same which cancels the operation
                if nums.index(second_value) == index:
                    continue
                list.append(index)
                list.append(nums.index(second_value))
                break
        return list

# This is a test object to run the class
dog = Solution()
print(dog.twoSum([-3, 4, 3, 90], 0))

