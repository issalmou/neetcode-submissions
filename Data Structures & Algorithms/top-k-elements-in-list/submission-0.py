class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        strr={}
        for i in nums:
            if i in strr.keys():
                strr[i]+=1
            else:
                strr[i]=1
        top_freq=list(strr.values())
        top_freq.sort(reverse=True)
        top_freq=top_freq[:k]
        result=[]
        for key,value in strr.items():
            if value in top_freq:
                result.append(key)
        return result