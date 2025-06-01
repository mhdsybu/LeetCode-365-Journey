Question: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


Sol_1:- Brute-Force Solution (O(n²))
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(f"Input list: {nums}")
        print(f"Target sum: {target}")
        
        for i in range(len(nums)):
            print(f"\nChecking index i={i}, value={nums[i]}")
            for j in range(i + 1, len(nums)):
                print(f"  Comparing with index j={j}, value={nums[j]}")
                sum_pair = nums[i] + nums[j]
                print(f"  Sum of nums[{i}] + nums[{j}] = {nums[i]} + {nums[j]} = {sum_pair}")
                
                if sum_pair == target:
                    print(f"  ✅ Found target sum: indices = [{i}, {j}]")
                    return [i, j]

        print("No two sum solution found.")
        return []

sol = Solution()
result = sol.twoSum([2, 7, 11, 15], 100)
print("\nFinal Output:", result)


Sol_2:- Optimized Solution Using Hash Map (O(n))
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        print(f"Input list: {nums}")
        print(f"Target sum: {target}\n")
        
        hashmap = {}  # This dictionary stores numbers as keys and their indices as values
        print("Initial empty hashmap:", hashmap)

        for i, num in enumerate(nums):
            complement = target - num
            print(f"\nChecking index {i} with number {num}")
            print(f"Complement needed for target: {complement}")

            if complement in hashmap:
                print(f"✅ Complement {complement} found in hashmap at index {hashmap[complement]}")
                print(f"Returning indices: [{hashmap[complement]}, {i}]")
                return [hashmap[complement], i]

            hashmap[num] = i  # Store the index of the current number
            print(f"Hashmap updated: {hashmap}")

        print("❌ No two numbers found that sum to target.")
        return []

sol = Solution()
result = sol.twoSum([2, 7, 11, 15], 9)
print("\nFinal Output:", result)
