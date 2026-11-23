class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # First, I sort the list which is given to me lexicographically
        # so, ['flower','flow','flight'] -> ['flight', 'flow', 'flower']
        # what we can see here is that the first and the last ones are the only ones to compare
        # since now the commoon prefix, if any, should be common to all the strings in the list

        ans = ""
        strs = sorted(strs)
        first, last = strs[0], strs[-1]
        for i in range(min(len(first), len(last))): # only have to look at the smaller string
            if first[i] != last[i]:
                return ans
            ans+=first[i]
        
        return ans