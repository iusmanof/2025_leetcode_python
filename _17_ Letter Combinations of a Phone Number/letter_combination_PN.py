class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        digitsToChar = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "qprs",
            8: "tuv",
            9: "wxyz"
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                result.append(curStr)
                return
            for c in digitsToChar[int(digits[i])]:
                backtrack(i + 1, curStr + c)

        if digits:
            backtrack(0, "")
            
        return result
    