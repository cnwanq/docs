class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # for item in s:
        #     if item == '(':
        #         stack.append(')')
        #     elif item == '[':
        #         stack.append(']')
        #     elif item == '{':
        #         stack.append('}')
        #     elif not stack or stack[-1] != item:
        #         return False
        #     else:
        #         stack.pop()
        # if stack:
        #     return False
        # return True
        start = []
        paren_map = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c not in paren_map:
                start.append(c)
            elif not start or paren_map[c] != start.pop():
                return False
        return not start

        