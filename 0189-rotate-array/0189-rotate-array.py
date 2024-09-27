class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        a=nums[-k:]
        b=nums[:len(nums)-k]
        a.extend(b)
        for i in range(len(nums)):
            nums[i]=a[i]