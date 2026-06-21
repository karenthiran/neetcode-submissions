class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i=0
        j=len(matrix[0])-1
        while i<len(matrix) and matrix[i][j]<target:
            i+=1
        if i==len(matrix):
            return False
        l=matrix[i]
        i=0
        while i<=j:
            mid=(i+j)//2
            if l[mid]==target:
                return True
            elif l[mid]>target:
                j=mid-1
            else:
                i=mid+1
        return False