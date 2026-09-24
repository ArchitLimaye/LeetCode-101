def twoSum(nums,trgt):
    dict={}
    count=0
    index_count=0
    for i in nums:
        diff=trgt-i
        if diff in dict:
            return count,dict[diff]
        else:
            dict[i]=count
            count+=1
#Test cases
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
