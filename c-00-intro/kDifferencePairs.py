# PAGE 80
# Given an array of distinct integer values, count the number of pairs of integers that have difference k.

# Example:

# Given the array [1, 7, 5, 9, 2, 12, 3] and difference k = 2
# Output: 4 | [1, 3], [3, 5], [5, 7], [7, 9]

# Time complexity: O(n), Space complexity: O(n)
def k_diff_pairs(arr, k):
  ht = {}
  pairs = 0

  for i in range(len(arr)):
    ht[i] = arr[i]

  for i in range(len(arr)):
    if ht[i] - k in ht:
      pairs += 1
  
  return pairs

print(k_diff_pairs([1, 7, 5, 9, 2, 12, 3], 2))