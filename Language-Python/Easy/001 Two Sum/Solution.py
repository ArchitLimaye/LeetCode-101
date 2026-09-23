#Two sum problem (Brute Force)
def twoSum(nums, target):
    index=[]
    for i in range(len(nums)):
        for j in range (i+1,len(nums)):
            if nums[i] + nums[j]==target:
                index.extend([i,j])
                return index
    return 
#Test Cases
test_cases = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([-10,2,8,5], -2)

]
count=1
for nums, target in test_cases:
    print("Input:", nums, "Target:", target)
    print("Output:", twoSum(nums, target))
    print("-" * 30,"Test Case:",count)
    count+=1
