class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l = 0
        o = 0
        for i in range(len(s)):
            maxCost -= abs(ord(s[i]) - ord(t[i]))
            while  maxCost < 0 :
                maxCost += abs(ord(s[l]) - ord(t[l]))
                l += 1
            o = max(o, i - l + 1)
        return o

