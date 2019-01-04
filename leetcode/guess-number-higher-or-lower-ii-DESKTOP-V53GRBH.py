import random
def guess(nums, maximum):
    if len(nums) <= 1:
        return 0
    min_cost = float("inf")
    random.shuffle(nums)
    print(nums)
    for num in nums: #选择策略
        # ans < num
        left = guess(nums[:nums.index(num)], 0)
        # ans > num
        right = guess(nums[nums.index(num) + 1:], left)
        cost = max(left, right) + num #最差ans
        if maximum and cost <= maximum: # α-β pruning
            min_cost = cost
            break
        else:
            min_cost = min(min_cost, cost)
    return min_cost #最优策略




print(guess(list(range(1,5)), 0))

