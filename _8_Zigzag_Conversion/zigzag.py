class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result = ""
        
        if numRows == 1: return s
        
        for row in range(numRows):
            incr = 2 *(numRows - 1)
            for i in  range(row, len(s), incr):
                result += s[i]
                if (row > 0 and row < numRows - 1 and i + incr - 2 * row < len(s)):
                    result += s[i + incr - 2 * row]
        
        return result
            
        