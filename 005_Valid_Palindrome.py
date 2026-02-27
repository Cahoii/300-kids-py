# Problem: Valid Palindrome
# URL: https://leetcode.com/problems/valid-palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Time Complexity: O(N), where N is the length of the string s.
        # In the worst case, both pointers traverse the entire string once.
        # Space Complexity: O(1).
        # No additional data structures are used that scale with the input size.

        left, right = 0, len(s) - 1

        while left < right:
            # Move the left pointer inwards until an alphanumeric character is found
            while left < right and not s[left].isalnum():
                left += 1
            
            # Move the right pointer inwards until an alphanumeric character is found
            while left < right and not s[right].isalnum():
                right -= 1
            
            # If characters at the current pointers do not match (case-insensitive),
            # the string is not a palindrome
            if left < right and s[left].lower() != s[right].lower():
                return False
            
            # Move both pointers inwards to check the next pair
            left += 1
            right -= 1
            
        # If the loop completes, all alphanumeric characters matched, meaning it's a palindrome
        return True