class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i]),
            countT[t[i]] = countT.get(t[i]),
        return countS == countT
        