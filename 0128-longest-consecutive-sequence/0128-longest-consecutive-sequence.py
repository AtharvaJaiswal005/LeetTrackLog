class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        l=0
        for i in s:
            if i-1 not in s:
                a=0
                while (i+a) in s:
                    a+=1
            l=max(a,l)
        return l