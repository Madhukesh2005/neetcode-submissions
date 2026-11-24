class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for x in nums:
            d[x]=d.get(x,0)+1
        
        res=[]
        keys=sorted(d,key=d.get,reverse=True)
        for i in range(k):
            res.append(keys[i])
        return res



            
        