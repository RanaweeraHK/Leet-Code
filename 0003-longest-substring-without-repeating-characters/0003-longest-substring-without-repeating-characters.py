class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        max_length = 0
        left = 0  # Left pointer of the sliding window

        for right in range(len(s)):
            # If the current character is already in the set,
            # move the left pointer to the right until the duplicate is removed
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            # Add the current character to the set
            char_set.add(s[right])

            # Update the maximum length if needed
            max_length = max(max_length, right - left + 1)

        return max_length


            
        