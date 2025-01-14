class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq={}
        t=[[] for i in range(len(nums)+1)]
        res=[]
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for i,j in freq.items():
            t[j].append(i)
        for i in range(len(t)-1,-1,-1):
            if t[i] and k!=0:
                print(t[i])
                res.extend(t[i])
                k-=1
        return res