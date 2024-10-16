class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        result = []
        balance = 0
        
        for char in s:
            if char == '(':
                # If this is the outermost '('
                if balance > 0:
                    result.append(char)
                balance += 1
            elif char == ')':
                # If this is the outermost ')'
                if balance > 1:
                    result.append(char)
                balance -= 1

        return ''.join(result)
