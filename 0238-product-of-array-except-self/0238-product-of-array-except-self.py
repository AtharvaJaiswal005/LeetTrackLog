class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        z=0
        for i in nums:
            if i==0:
                z+=1
        if z>1:
            res=[0]*len(nums)
            return res
        for j in range(len(nums)):
            t=1
            for i in range(len(nums)):
                if i!=j:
                    t*=nums[i]
            res.append(t)
        return res