class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=""
        for i in digits:
            s+=str(i)
        digits=str(int(s)+1)
        return [int(i) for i in digits]
        