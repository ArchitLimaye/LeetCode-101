# Palindrome Number

**LeetCode #9**  
![Easy](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.


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

[String reversal Solution](./String%20Reversal%20Approach.py)

---

### 2. Mathematical Approach

**Approach:**  
I reversed the number using mathematical approach using Arithmetic Operators like modulo(%) and Floor Division (//).

I used `% 10` to get the last digit and `// 10` to remove the last digit. The extracted digits were stored in `rev`.

Once the reversed num was saved in `rev` variable I compared it with the `num_copy` which stored the num at the start and returned thier comparision .

For numbers with an odd number of digits, the middle digit can be ignored while comparing the two halves.

**Time Complexity:** `O(log x)`

**Space Complexity:** `O(1)`

[View Optimal Solution](./Mathematical%20Approach.py)
