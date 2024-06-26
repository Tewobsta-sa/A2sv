#using recurssion
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.rev(s,0, len(s)-1)
    def rev(self,s, i, j):
        if i >=j:
            return 
        else:
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
            self.rev(s,i,j)
#other way
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        while i <= j:
            s[i], s[j] = s[j],s[i]
            i+=1
            j-=1 
        
