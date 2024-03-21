class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandFromCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]  # Return the palindrome substring
        
        longest_palindrome = ""
        
        for i in range(len(s)):
            # Case 1: Palindrome with odd length (centered at i)
            palindrome_odd = expandFromCenter(i, i)
            # Case 2: Palindrome with even length (centered at i and i+1)
            palindrome_even = expandFromCenter(i, i + 1)
            
            # Update longest_palindrome if a longer palindrome is found
            if len(palindrome_odd) > len(longest_palindrome):
                longest_palindrome = palindrome_odd
            if len(palindrome_even) > len(longest_palindrome):
                longest_palindrome = palindrome_even
                
        return longest_palindrome
