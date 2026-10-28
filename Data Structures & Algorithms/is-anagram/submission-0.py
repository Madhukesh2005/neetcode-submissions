class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        new_s="".join(sorted(s))
        new_t="".join(sorted(t))
        return new_s==new_t