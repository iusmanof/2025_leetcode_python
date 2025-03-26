class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map_brackets = { ')': '(', ']': '[', '}': '{'}
        stack = []
        
        
        for br in s:
            if br not in map_brackets:
                stack.append(br)
            else:
                if not stack:
                    return False
                else:
                    popped = stack.pop()
                    if popped != map_brackets[br]: 
                        return False
        
        return not stack    