class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numss={}

        for i , num in enumerate(nums):
            need= target-num

            if need in numss:
                return[numss[need],i]
            
            numss[num]=i
        