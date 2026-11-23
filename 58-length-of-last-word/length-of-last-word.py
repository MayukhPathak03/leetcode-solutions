class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        x = s.strip()
        y = x.rsplit(" ")
        z = y[-1]
        return len(z)