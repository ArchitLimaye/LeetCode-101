def isPalindrome(nums):
    if nums == nums[::-1]:
        return True

num=int(input("Please enter a number to check if its a palindrome:"))
num=str(num)
print(num,"Shows Palindrom Pattern:",isPalindrome(num))