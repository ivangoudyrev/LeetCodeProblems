class Solution(object):
    def isValid(self, s):
        stack = []
    
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif len(stack) > 0:
                close = stack.pop()
                if char == ')' and close != '(':
                    return False
                elif char == ']' and close != '[':
                    return False
                elif char == '}' and close != '{':
                    return False
            else:
                return False
        
        if len(stack) == 0:
            return True
        else:
            return False
        
        """
        :type s: str
        :rtype: bool
        """