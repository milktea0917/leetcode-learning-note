# Version2: Dict -> 

# A dict() to help solve the problem in one pass
class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]]=i
            else:
                return[dict[target-nums[i]], i]
            
####
# Version1: Brute Force -> O(n^2)

# final_return_list: list we return in final
# difference: deference of two number 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final_return_list = []
        
        for index_num, content in enumerate(nums):
            difference = target - content
            if difference in nums[index_num+1:]:
                    difference_index = nums[index_num+1:].index(difference)
                    final_return_list.append(index_num)
                    final_return_list.append(difference_index + index_num + 1)
                    return final_return_list
