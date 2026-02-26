# Problem: Valid Parentheses
# URL: https://leetcode.com/problems/valid-parentheses
# Difficulty: Easy
# Topics: String, Stack
class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time Complexity: O(N), where N is the length of the string s.
                         We iterate through the string once, and stack operations (append, pop, peek)
                         take O(1) on average. Dictionary lookups are also O(1) on average.
        Space Complexity: O(N), in the worst case, the stack can store up to N/2 opening brackets
                          (e.g., "((((((....)))))").
        """
        stack = []
        # A dictionary to map closing brackets to their corresponding opening brackets.
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char in mapping:  # If the character is a closing bracket
                # If the stack is empty, or the top of the stack does not match
                # the expected opening bracket for the current closing bracket,
                # then the string is invalid.
                if not stack or stack[-1] != mapping[char]:
                    return False
                # If it matches, pop the opening bracket from the stack.
                stack.pop()
            else:  # If the character is an opening bracket
                # Push the opening bracket onto the stack.
                stack.append(char)
        
        # After iterating through all characters, if the stack is empty, it means
        # all opening brackets have been correctly closed and matched.
        # Otherwise, there are unclosed opening brackets, making the string invalid.
        return not stack