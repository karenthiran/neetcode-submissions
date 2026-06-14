class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        zero=0
        for i in nums:
            if i==0:
                zero+=1
            else:
                product*=i
        if zero>1:
            return [0]*len(nums)
        ans=[]
        for i in nums:
            if i==0:
                ans.append(product)
            elif zero==1:
                ans.append(0)
            else:
                ans.append(product//i)
        return ans