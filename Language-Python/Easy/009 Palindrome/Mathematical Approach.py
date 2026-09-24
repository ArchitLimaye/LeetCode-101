def isPalindrome(num):
    num_copy=num
    rev=0
    if num<0:
        return False
    while num>0:
        rev=(rev*10)+num%10
        num//=10

    return num_copy == rev
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
