class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        lp=1
        ans=[]
        for i in range(n):
            ans.append(lp)
            lp*=nums[i]
        rp=1
        for i in range(n-1,-1,-1):
            ans[i]*=rp
            rp*=nums[i]
        return ans