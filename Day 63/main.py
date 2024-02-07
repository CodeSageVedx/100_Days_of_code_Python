# Multiply Strings
#Solution1
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1 = int(num1)        
        num2 = int(num2)
        return str(num1*num2)

#Solution 2
class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        return f"{int(num1) * int(num2)}"
        
        n1,n2 = 0,0
        for i in num1:
            n1 = n1*10 + (ord(i)-48)
        for i in num2:
            n2 = n2*10 + (ord(i)-48)
        return f"{n1*n2}"