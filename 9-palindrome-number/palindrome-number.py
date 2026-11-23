class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        y,a,z=x,0,0
        while y>=10:
            z=y%10
            y=int(y/10)
            a=(a+z)*10
        a=a+y
        if a==x:
            return True
        else:
            return False