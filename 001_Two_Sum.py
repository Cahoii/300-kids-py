# Problem: Two Sum
# URL: https://leetcode.com/problems/two-sum
# Difficulty: Easy
# Topics: Array, Hash Table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # A hash map (dictionary in Python) to store numbers and their indices.
        # Key: number, Value: index
        # This allows O(1) average time complexity for lookups and insertions.
        # Space complexity: O(N) in the worst case, where N is the number of elements in nums,
        # as we might store all elements in the hash map.
        num_map = {}

        # Iterate through the array `nums` once.
        # Time complexity: O(N), where N is the number of elements in nums.
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target sum.
            complement = target - num

            # Check if the complement exists in our hash map.
            # If it does, we have found the two numbers that sum up to the target.
            # Average time complexity for dictionary lookup is O(1).
            if complement in num_map:
                # Return the index of the complement (stored in num_map)
                # and the index of the current number (i).
                return [num_map[complement], i]
            
            # If the complement is not found, add the current number and its index
            # to the hash map. This prepares for future lookups.
            # Average time complexity for dictionary insertion is O(1).
            num_map[num] = i
        
        # The problem statement guarantees that exactly one solution exists.
        # Therefore, the loop will always find a pair and return before reaching this point.