class Solution:
    def searchInsert(name, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

list = Solution()
nums = []
n = int(input("How many numbers you want to enter ? "))
for i in range(n):
    num = int(input("Enter the number : "))
    nums.append(num)
target=int(input("Enter a target number : "))
print("Input : ","nums = ",nums, ", ","target = ",target)
print("Output : ",list.searchInsert(nums, target))