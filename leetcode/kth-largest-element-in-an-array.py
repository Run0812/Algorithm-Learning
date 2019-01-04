import random

def partition(nums, left, right):
    p = random.randint(left, right)
    nums[p], nums[right] = nums[right], nums[p]
    i = left - 1
    for j in range(left, right):
        if nums[j] <= nums[right]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[right] = nums[right], nums[i+1]
    # print(nums[p])
    return i+1

def quickSort(nums, left, right):
    if left < right:
        q = partition(nums, left, right)
        quickSort(nums, left, q-1)
        quickSort(nums, q+1, right)
    return

def select(nums, left, right, k):
    # print(nums[left:right+1], k)
    if left == right:
        # return nums[left]
        return left
    p = partition(nums, left, right)
    pos =  len(nums) - p
    if pos == k:
        # return nums[p]
        return p
    elif pos > k:
        return select(nums, p+1, right, k)
    else:
        return select(nums, left, p-1, k)

def bubble_sort(nums, left, right):
    for j in range(right - left + 1):
        for pick in range(left, right - j):
            if nums[pick] > nums[pick + 1]:
                nums[pick], nums[pick + 1] = nums[pick + 1], nums[pick]
    return

def search(nums,k):
    l = len(nums)
    if l == 1:
        return nums[0]
    # TODO:不需要开辟新内存，直接调取间隔5的元素作为midline 2 7 12...:
    for i in range(l//5):
        bubble_sort(nums,i ,i+4)
    mid_line = [nums[j+2] for j in range(l//5)]
    if l % 5:
        bubble_sort(nums,l-1-(l%5),l-1)
        mid_line.append(-(l%5))
    p = select(mid_line, 0, len(mid_line)-1, len(mid_line)//2+1)

    # nrow = l // 5
    # g =[]
    # for i in range(nrow):
    #     g.append(sorted(nums[5*i:5*i+5]))
    # if l % 5:
    #     nrow += 1
    #     g.append(sorted(nums[-(l%5):]))
    # mid_line = [row[len(row)//2] for row in g]
    # p = select(mid_line, 0, len(mid_line)-1, len(mid_line)//2+1)


    nums[p], nums[-1] = nums[-1], nums[p]
    pos_i = 0
    for j in range(l):
        if nums[j] < nums[-1]:
            nums[pos_i], nums[j] = nums[j], nums[pos_i]
            pos_i += 1
    nums[pos_i], nums[-1] = nums[-1], nums[pos_i]
    pth = l - pos_i
    if pth == k:
        return nums[pos_i]
    elif pth > k:
        return search(nums[pos_i+1:], k)
    else:
        return search(nums[:pos_i], k - pth)


def findKthLargest(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # sol 1
    # nums.sort()
    # return nums[-k]
    # sol 2
    # return select(nums, 0, len(nums)-1, k)
    # sol 3
    return search(nums,k)




nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
k = 1
ans = findKthLargest(nums, k)
print(ans)
# print(findKthLargest(nums, k))