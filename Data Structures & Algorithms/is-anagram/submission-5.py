class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t)!=len(s) or len(s)<1 or len(t)>(5*10000):
            return False
        t=''.join(sorted(t))
        s=''.join(sorted(s))
        return t==s