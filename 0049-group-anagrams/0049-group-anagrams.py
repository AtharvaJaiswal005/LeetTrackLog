class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        s=defaultdict(list)
        a=[0]*26
        for i in strs:
            for j in i:
                k=ord(j)-ord("a")
                a[k]+=1
            s[tuple(a)].append(i)
            a=[0]*26
        return s.values()