class Solution:
    def isValid(self, s: str) -> bool:
        # eg1:
        # stack = []
        # for i in range(len(s)):
        #     if len(stack) == 0 and (s[i] == ')' or s[i] == ']' or s[i] == '}'):
        #         return False
        #     if s[i] == '(' or s[i] == '[' or s[i] == '{':
        #         stack.append(s[i])
        #     elif s[i] == ')' and stack[-1] != '(':
        #         return False
        #     elif s[i] == ']' and stack[-1] != '[':
        #         return False
        #     elif s[i] == '}' and stack[-1] != '{':
        #         return False
        #     else:
        #         stack.pop()
        # if len(stack) > 0:
        #     return False
        # else:
        #     return True
        # eg2:
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        return len(stack) == 1

a= Solution()
print(a.isValid("()[]{}"))