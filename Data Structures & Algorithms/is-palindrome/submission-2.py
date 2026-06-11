class Solution:
    def isPalindrome(self, s: str) -> bool:
        st=''.join(s.split(" "))
        st=st.lower()
        j=len(st)-1  
        i=0
        while i<j:
            n=ord(st[i])
            m=ord(st[j])
            if (m<47 or m>57) and (m>122 or m<97):
                j-=1
                continue
            if (n<47 or n>57) and (n>122 or n<97):
                i+=1
                continue
            if st[i]!=st[j]:
                return False
            i+=1
            j-=1
        return True