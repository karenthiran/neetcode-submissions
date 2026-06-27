class Solution:
    def trap(self, height: List[int]) -> int:
        ans=0
        i,j=0,len(height)-1
        while i<len(height)-1 and height[i]<height[i+1]:
            i+=1
        left=height[i]
        while i>0 and height[j]<height[j-1]:
            j-=1
        right=height[j]
        while i<j:
            h=min(right,left)
            if height[i]>left:
                left=height[i]
            elif height[j]>right:
                right=height[j]
            elif left>right:
                ans+=right-height[j]
                j-=1
            else:
                ans+=left-height[i]
                i+=1
        return ans