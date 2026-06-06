class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        
        lst=[]

        for i in s:
            lst.append(i)
        for i in t:
            if i not in lst:
                return False
            else:
                lst.remove(i)
        return len(lst)==0