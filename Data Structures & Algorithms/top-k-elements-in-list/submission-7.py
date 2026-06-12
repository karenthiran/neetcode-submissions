class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        ans=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        d2=defaultdict(list)
        for key,v in d.items():
            d2[v].append(key)
        for j in range(len(nums),-1,-1):
            l=d2[j]
            i=0
            while len(ans)<k and i<len(l):
                ans.append(l[i])
                i+=1
        return ans