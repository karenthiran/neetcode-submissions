class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0;
        j=len(nums)-1
        res=[]
        if nums[j]<0:
            target=abs(target);
        while i<j:
            t=abs(nums[i]+nums[j])
            if t==target:
                res.append(i)
                res.append(j)
                return res
            elif t>target:
                j-=1
            else:
                i+=1
        return res    