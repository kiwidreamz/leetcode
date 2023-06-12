class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        bracket_map = {")": "(", "}": "{", "]": "["}
        open_brackets = set(["(", "{", "["])

        for i in s:
            if i in open_brackets:
                stack.append(i)
            elif stack and bracket_map[i] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []