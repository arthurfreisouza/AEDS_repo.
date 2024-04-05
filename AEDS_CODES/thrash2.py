array = list(map(float, [-4, -1, 0, 3, 10]))

def sortedSquares(nums):
    nums = list(map(float, nums))
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    print(nums)
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                aux = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = aux          
    nums =  list(map(int, nums))

sortedSquares(array)