class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range (0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    indices=[i,j]

        return indices
                
# mistakes 
# initially used list() method to make a list of integers i and j but it wont work
# as i and j are just integers and are not iterables
# so for non iterables we use ournewlist=[i,j] and another mistake was
# sorting the array by default this question is index specific hence sorting the
# array changes indices so dont blindly sort the array everytime
# apparently can do it in O(n) using hashmap
        