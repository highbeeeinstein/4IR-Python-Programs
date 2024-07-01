def productExceptSelf(nums):
    n = len(nums)
    answer = [1] * n
    left_product =1
    for i in range(n):
        answer[i] *= left_product
        left_product *= nums[i]
    right_product = 1
    for i in range(n-1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]
    return answer
print(productExceptSelf([3,4,5,6]))
ans = [1]
print(ans * 4)