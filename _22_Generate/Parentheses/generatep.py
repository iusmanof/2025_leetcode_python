class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []
        solution = []
        
        def backtrack(openB, closeB):
            if len(solution) == 2*n:
                answer.append(''.join(solution))
                
            if openB < n:
                solution.append('(')
                backtrack(openB + 1, closeB )
                solution.pop()
                
            if openB > closeB:
                solution.append(")")
                backtrack(openB, closeB + 1)
                solution.pop()
                
        backtrack(0,0)
        return answer