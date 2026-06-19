class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        lst=[]
        for i in tokens:
            if i=='+' or i=='-' or i=='/' or i=='*':
                a=lst.pop()
                b=lst.pop()
                if i=='-':
                    lst.append(b-a)
                elif i=='+':
                    lst.append(b+a)
                elif i=='*':
                    lst.append(a*b)
                else:
                    x=b/a
                    lst.append(int(x))
            else:
                lst.append(int(i))
        return lst[0]