class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(nums)
        n=len(nums)
        m=1
        l=[]
        if n==0:
            return 0
        for i in range(n-1):
            if nums[i]==nums[i+1] :
                continue
            if nums[i]+1==nums[i+1]:
                m+=1
            else:
                l.append(m)
                m=1
        l.append(m)
        return max(l)