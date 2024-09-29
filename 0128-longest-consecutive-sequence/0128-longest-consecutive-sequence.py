class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset=set(nums)
        lcs=0
        for i in nums:
            if not i-1 in hset:
                l=1
                while i+l in hset:
                    l+=1
                lcs=max(lcs,l)
        return lcs