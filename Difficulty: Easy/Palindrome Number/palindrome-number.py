class Solution:
    def isPalindrome(self, n):
        original = n

        # Handle negative numbers
        n = abs(n)

        rev = 0

        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n //= 10

        return abs(original) == rev