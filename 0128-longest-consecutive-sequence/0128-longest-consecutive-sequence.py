class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        nums=set(nums)
        leng=0
        longi=0
        for i in nums:
            if i-1 not in nums:
                leng=1
                while i+leng in nums:
                    leng+=1
            longi=max(longi,leng)
        return longi