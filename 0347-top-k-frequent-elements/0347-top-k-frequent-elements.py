class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import defaultdict
        
        # Step 1: Count the frequency of each number
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # Step 2: Create a frequency bucket where keys are counts
        bucket = defaultdict(list)
        for num, count in freq.items():
            bucket[count].append(num)
        
        # Step 3: Sort the frequencies in descending order
        sorted_freqs = sorted(bucket.keys(), reverse=True)
        
        # Step 4: Collect the top K frequent elements
        result = []
        for freq_count in sorted_freqs:
            result.extend(bucket[freq_count])  # Add all elements with the same frequency
            if len(result) >= k:  # Stop if we already have k elements
                return result[:k]  # Return exactly k elements
