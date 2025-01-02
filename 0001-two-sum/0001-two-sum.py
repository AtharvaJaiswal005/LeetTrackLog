class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d={}
        for i,j in enumerate(nums):
            dif=target-j
            if dif in d:
                return [d[dif],i]
            d[j]=i
                