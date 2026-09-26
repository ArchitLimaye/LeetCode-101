# Roman to Integer

**LeetCode 13**
![Easy](https://img.shields.io/badge/Difficulty-Easy-green)
## Problem

Roman numerals are represented by seven different symbols:

```text
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
```

Given a Roman numeral, convert it to an integer.

### Example

```text
Input:
s = "III"

Output:
3
```

```text
Input:
s = "LVIII"

Output:
58
```

```text
Input:
s = "MCMXCIV"

Output:
1994
```

## Different Approaches Used

### 1. Conditional Approach

**Approach:**

I traversed the Roman numeral from right to left and used conditional statements to identify each Roman symbol.

For subtractive combinations such as `IV`, `IX`, `XL`, `XC`, `CD`, and `CM`, I directly checked the previous character and added their combined value. A `char` variable was used to skip the character that had already been processed as part of a combination.

**Time Complexity:** `O(n)`

**Space Complexity:** `O(1)`

[View Conditional Solution](https://github.com/ArchitLimaye/LeetCode-101/blob/main/Language-Python/Easy/013%20Roman%20to%20Integer/Conditional%20Approach.py)

---

### 2. Mapping Approach

**Approach:**

I stored the value of each Roman symbol in a dictionary. I then traversed the Roman numeral from right to left while keeping track of the previous value.

If the current value was smaller than the previous value, it was subtracted from the total. Otherwise, it was added.

This approach handles subtractive combinations automatically without explicitly checking for `IV`, `IX`, `XL`, `XC`, `CD`, or `CM`.

**Time Complexity:** `O(n)`

**Space Complexity:** `O(1)`

[View Mapping Solution](https://github.com/ArchitLimaye/LeetCode-101/blob/main/Language-Python/Easy/013%20Roman%20to%20Integer/Mapping%20Approach.py)
