class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        f={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for i,j in d.items():
            f[j]=i
        s=sorted([i for i in f.keys()],reverse=True)
        return [f[i] for i in s][:k]