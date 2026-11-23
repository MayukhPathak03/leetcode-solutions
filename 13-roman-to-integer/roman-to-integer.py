class Solution:
    def romanToInt(self, s: str) -> int:
        store = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        main_value = 0
        for i in range(len(s)):
            if i < (len(s)-1) and store.get(s[i]) < store.get(s[i+1]):
                main_value -= store.get(s[i])
            else:
                main_value += store.get(s[i])
        return main_value