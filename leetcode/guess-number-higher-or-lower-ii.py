import random
def guess(nums, maximum):
    if len(nums) <= 1:
        return 0
    min_cost = float("inf")
    random.shuffle(nums)
    for num in nums: #选择策略
        # ans > num
        right = guess(nums[nums.index(num) + 1:], 0)

        # ans < num
        left = guess(nums[:nums.index(num)], right)

        cost = max(left, right) + num #最差ans
        if maximum and cost <= maximum: # α-β pruning
            min_cost = cost
            break
        else:
            min_cost = min(min_cost, cost)
    return min_cost #最优策略

# dp method

def guess2(n):
    ans = [0, 0, 1]
    times  = [0, 1, 2]
    for i in range(3, n + 1):
        min_cost = float("inf")
        for j in range(i//2, i):
            if ans[j - 1] >= (times[i-j]-1)*j + ans[i - j]:
                cost = j+ans[j - 1]
                time = times[j-1]
            else:
                cost =j+(times[i-j]-1)*j + ans[i - j] # 计算cost错误 当j变大后最优取法会变化
                time = times[i-j]
            # cost = j + max(ans[j - 1], (times[i-j]-1)*j + ans[i - j])
            if cost < min_cost:
                min_cost = cost
                min_time = 1 + time
        ans.append(min_cost)
        times.append(min_time)
    print(ans)
    print(times)
    return ans[n]


# print(guess(list(range(1, 4)), 0))
print(guess2(9))

# choice = list(range(1, n + 1))
# mincash = [-1] * n
# for ans in range(1, n + 1):

