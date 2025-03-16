class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        listN = [int(x) for x in str(x)]
        for i in range(len(listN)//2):
            if listN[i] != listN[len(listN) - 1 - i]:
                return False

        return True
            