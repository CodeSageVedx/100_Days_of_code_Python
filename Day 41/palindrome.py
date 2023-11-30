class Solution:
    @staticmethod
    def isPalindrome(x):
        if x < 0:
            return False

        reversed_num = 0
        temp = x

        while temp != 0:
            digit = temp % 10
            reversed_num = reversed_num * 10 + digit
            temp //= 10

        return x == reversed_num

# Create an instance of the Solution class
solution_instance = Solution()

# Call the isPalindrome method on the instance
result = solution_instance.isPalindrome(121)

# Print the result
print(result)
