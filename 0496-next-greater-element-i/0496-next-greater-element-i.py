class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge_map = {}
        stack = []
        
        for num in nums2:
            while stack and num > stack[-1]:
                small_num = stack.pop()
                nge_map[small_num] = num
            stack.append(num)
        
        while stack:
            small_num = stack.pop()
            nge_map[small_num] = -1
        
        return [nge_map[num] for num in nums1]