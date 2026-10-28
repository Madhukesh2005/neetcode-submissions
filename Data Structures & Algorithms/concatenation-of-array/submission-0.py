class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[0]*(2*len(nums))
        ans[:len(nums)]=nums
        ans[len(nums):]=nums
        return ans