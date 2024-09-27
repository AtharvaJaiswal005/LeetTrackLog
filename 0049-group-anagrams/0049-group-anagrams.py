class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            s=tuple(sorted(i))
            d[s]=[]
        for i in strs:
            s=tuple(sorted(i))
            d[s].append(i)
        return list(d.values())