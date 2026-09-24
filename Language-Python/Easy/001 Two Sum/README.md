# Two Sum

**LeetCode #1**  
![Easy](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are given an array of integers `nums` and an integer `target`. Return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Example

```text
Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]
```

## Different Approaches Used

### 1. Using Nested Loops

**Approach:**  
Using nested loops, I compared each element with the other elements in the list. If the sum of two elements matched the target, I returned their indices.

**Time Complexity:** `O(n²)`

**Space Complexity:** `O(1)`

[View Brute Force Solution](./Nested%20Loop%20Approach.py)

---

### 2. Using HashMap

**Approach:**  
Using a HashMap (Python dictionary), I stored all the elements that I had already seen along with their indices.

While looping through the list, I calculated the difference between the target and the current element. I then checked if that difference was already present in the HashMap.

If the difference was found, I returned the index of the current element and the index stored for the matching difference.

**Time Complexity:** `O(n)`

**Space Complexity:** `O(n)`

[View Optimal Solution](./HashMap%20Approach.py)
