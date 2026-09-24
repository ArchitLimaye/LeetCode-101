def isPalindrome(nums):
    nums=str(nums)
    if nums == nums[::-1]:
        return True
#Test Cases
test_cases = [
    1221,
    10,
    -123,
    12321,
    111

]
print("``````Test Cases```````")
count=1
for nums in test_cases:
    print("Input:", nums)
    print("Output:", isPalindrome(nums))
    print("-" * 30,"Test Case:",count)
    count+=1
