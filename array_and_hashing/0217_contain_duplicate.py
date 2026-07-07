"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

DIFFICULTY LEVEL: Easy

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n)
 
"""

def containsDuplicate(nums):
        hashset=set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False

print(containsDuplicate([1,2,3,1]))  # Output: True