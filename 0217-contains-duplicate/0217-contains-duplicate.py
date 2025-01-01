class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s=set(nums)
        f={i:0 for i in s}
        for i in nums:
            f[i]+=1
        for i in f.values():
            if i>1:
                return True
        return False