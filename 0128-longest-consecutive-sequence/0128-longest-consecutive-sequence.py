class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset=set(nums)
        lcs=0
        for i in hset:
            if i-1 not in hset:
                l=0
                while i+l in hset:
                    l+=1
                lcs=max(lcs,l)
        return lcs