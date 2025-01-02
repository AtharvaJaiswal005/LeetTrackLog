class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        s=[''.join(sorted(i)) for i in strs]
        s1=set(s)
        d={i:[] for i in s1}
        for i in range(len(s)):
            d[s[i]].append(strs[i])
        return list(d.values())
        