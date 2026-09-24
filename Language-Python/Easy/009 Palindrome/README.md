# Palindrome Number

**LeetCode #9**  
![Easy](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

A palindrome is a number that reads the same forward and backward.

### Example

```text
Input:
x = 121

Output:
true
```

```text
Input:
x = -121

Output:
false
```

## Different Approaches Used

### 1. String Reverse

**Approach:**  
I converted the number into a string and compared it with its reversed version using string slicing.

If both strings were the same, the number was a palindrome.

**Time Complexity:** `O(log x)`

**Space Complexity:** `O(log x)`

[View Brute Force Solution](./Brute_Force.py)

---

### 2. Optimal Solution

**Approach:**  
Instead of converting the number into a string, I reversed only half of the number.

I used `% 10` to get the last digit and `// 10` to remove the last digit. The extracted digits were stored in `reversed_half`.

Once half of the number was reversed, I compared it with the remaining half.

For numbers with an odd number of digits, the middle digit can be ignored while comparing the two halves.

**Time Complexity:** `O(log x)`

**Space Complexity:** `O(1)`

[View Optimal Solution](./Optimal_Solution.py)
