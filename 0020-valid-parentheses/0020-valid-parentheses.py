class Solution(object):
    def isValid(self, s):
        if(len(s)%2==1):
            return False
        stack =[]
        
        opening_brackets = {'(','[','{'}
        closing_brackets = {')':'(',']':'[','}':'{'}
        
        for char in s:
            if(char in opening_brackets):
                stack.append(char)
            
            elif (char in closing_brackets):
                if not stack or stack.pop()!= closing_brackets[char]:
                    return False
        
        return not stack