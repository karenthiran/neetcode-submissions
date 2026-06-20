class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        st=set()
        nums.sort()
        for i in range(len(nums)-2):
            n,m=i+1,len(nums)-1
            while n<m:
                a=nums[i]+nums[n]+nums[m]
                if a==0:
                    st.add(tuple(sorted([nums[i],nums[n],nums[m]])))
                    n+=1
                elif a<0:
                    n+=1
                else:
                    m-=1
        return list(st)