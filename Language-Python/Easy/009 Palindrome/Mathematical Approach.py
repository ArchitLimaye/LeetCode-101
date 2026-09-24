def isPalindrome(num):
    num_copy=num
    rev=0
    if num<0:
        return False
    while num>0:
        rev=(rev*10)+num%10
        num//=10

    return num_copy == rev
num=int(input("Please enter a number to check if its a palindrome:"))
print(num,"Shows Palindrom Pattern:",isPalindrome(num))