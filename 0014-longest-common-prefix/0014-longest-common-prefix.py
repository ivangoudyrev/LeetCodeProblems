import re

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        output = ""
        base = list(strs[0])
        prefix = ""
            
        if len(base) == 0:
            return ""

        if len(strs) == 1:
            return strs[0]
        
        for i in base:
            prefix += i
            for word in strs[1:]:
                if word.startswith(prefix):
                    pass
                else:
                    return output
            output = prefix
            
        return output
                    


