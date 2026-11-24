class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for s in strs:
            res.append(f"{len(s)}#{s}")
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        ans=[]
        length=0
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            i=j+1
            ans.append(s[i:i+length])
            i+=length
        return ans



