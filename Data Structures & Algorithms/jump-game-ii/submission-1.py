class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return 0

        goal=len(nums)-1
        jumps=0
        farthest=0
        border=0
        for i in range(len(nums)-1):
            look_ahead=i+nums[i]
            if look_ahead>farthest:
                farthest=look_ahead
            if border==i:
                jumps+=1
                border=farthest
            if border>=goal:
                return jumps
