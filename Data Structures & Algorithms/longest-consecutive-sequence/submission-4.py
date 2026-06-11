class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        st=set(nums)
        ans=0
        t=1
        for i in nums:
            if i-1 not in st:
                a=i
                while a+1 in st:
                    t+=1
                    a+=1
                ans=max(ans,t)
            t=1
        return ans