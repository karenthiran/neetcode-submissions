class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if len(stack)==0 and (i=='}' or i==')' or i==']'):
                return False
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            elif i==')' and stack[-1]=='(':
                stack.pop()
            elif i==']' and stack[-1]=='[':
                stack.pop()
            elif i=='}' and stack[-1]=='{':
                stack.pop()
            else:
                stack.append(i)
            
        if len(stack)!=0:
            return False
        return True