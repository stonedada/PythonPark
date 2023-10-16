class Solution:
    def isValid(self, s: str) -> bool:
        mid = len(s)//2
        left = s[:mid]
        right = s[mid:]
        for i in range(len(left)):
            if left[i] != right[-(i+1)]:
                return False

        return True

s = '"()[]{}"'
s1 ="()"
a= Solution()
print(a.isValid(s1))