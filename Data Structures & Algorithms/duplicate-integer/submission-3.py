class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)<0 or len(nums)>100000:
            return False
        ocr={}
        for i in nums :
            if i<-1000000000 or i>1000000000:
                return False
            if ocr.get(i,None):
                return True
            else:
                ocr[i]=1
        else:
            return False
        