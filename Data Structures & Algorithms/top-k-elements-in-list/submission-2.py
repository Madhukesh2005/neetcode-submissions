class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for x in nums:
            d[x]=d.get(x,0)+1

        buckets=[[] for _ in range(len(nums)+1)]

        for num,freq in d.items():
            buckets[freq].append(num)

        res=[]
        for i in range(len(buckets)-1,0,-1):
            for val in buckets[i]:
                res.append(val)
                if len(res)==k:
                    return res
        
            
        