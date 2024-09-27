class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map=dict()
        e=[]
        if len(s)!=len(t):
            print(False)
        for i in range(len(s)):
            if map.get(s[i],False):
                pass
            else:
                if t[i] not in e:
                    map[s[i]]=t[i]
                    e.append(t[i])
                else:
                    return False
        o=[]
        for i in s:
            o.append(map[i])
        c="".join(o)
        return c==t