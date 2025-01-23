class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ct=''.join([i.lower() for i in s if i.isalnum()])
        l=0;r=len(ct)-1
        while l<r:
            if ct[l]!=ct[r]:
                return False
            l+=1
            r-=1
        return True