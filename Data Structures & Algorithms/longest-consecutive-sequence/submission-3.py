class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        res = sorted(set(nums)) # Removes duplicates in O(N), sorts in O(N log N)
        maxcount = 1
        count = 1
        
        for i in range(1, len(res)):
            if res[i] == res[i - 1] + 1:
                count += 1
            else:
                maxcount = max(maxcount, count)
                count = 1
                
        return max(maxcount, count)


        



