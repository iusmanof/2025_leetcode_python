class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        resultLen = 0

        for idx in range(len(s)):
            # odd len
            l, r = idx, idx
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resultLen:
                    result = s[l:r+1]
                    resultLen = r - l + 1
                l -= 1
                r += 1
                
            # even len
            l, r = idx, idx + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resultLen:
                    result = s[l:r+1]
                    resultLen = r - l + 1
                l -= 1
                r += 1
                
            
        return result