
def intersection_union(sorted):
    intersection = []
    union = sorted[:]
    for i in range(len(sorted)-1):
        if sorted[i] == sorted[i+1]:
            intersection.append(sorted[i])
            union.remove(sorted[i])
    print('intersection:\n', intersection)
    print('union:\n', union)
    return intersection, union


def bubble_sort(for_sort):
    length = len(for_sort)
    for i in range(length-1):
        for j in range(length-i-1):
            if for_sort[j] > for_sort[j+1]:
                for_sort[j], for_sort[j+1] = for_sort[j+1], for_sort[j]
    return for_sort


def cocktail_sort(for_sort):
    length = len(for_sort)
    loop_time = length // 2  # floor divide
    left = 0
    right = length - 1
    for i in range(loop_time):
        for j in range(left, right):
            if for_sort[j] > for_sort[j + 1]:
                for_sort[j], for_sort[j + 1] = for_sort[j + 1], for_sort[j]
        right -= 1
        for j in range(right, left, -1):
            if for_sort[j] < for_sort[j - 1]:
                for_sort[j], for_sort[j - 1] = for_sort[j - 1], for_sort[j]
        left += 1
    return for_sort


def selection_sort(for_sort):
    length = len(for_sort)
    for i in range(length-1):
        min = i
        for j in range(i, length-1):
            if for_sort[j] < for_sort[min]:
                min = j
        for_sort[i], for_sort[min] = for_sort[min], for_sort[i]
    return for_sort


def insertion_sort(for_sort):
    length = len(for_sort)
    for i in range(length-1):
        pick = for_sort[i + 1]
        for j in range(i + 1):
            if pick < for_sort[j]:
                for_sort[j], pick = pick, for_sort[j]
        for_sort[i + 1] = pick
    return for_sort


def insertion_sort_dichotomy(for_sort):
    length = len(for_sort)
    for i in range(length - 1):
        pick = for_sort[i + 1]
        left = 0
        right = i
        while left <= right:
            mid = (left + right) // 2
            if pick < for_sort[mid]:
                right = mid - 1
            else:
                left = mid + 1
        for j in range(i + 1, left, -1):
            for_sort[j] = for_sort[j-1]
        for_sort[left] = pick
    return for_sort


def shell_sort(for_sort):
    length = len(for_sort)
    h = 1
    while h < length / 3:  # calculate the gap
        h = h * 3 + 1
    while h >= 1:
        for i in range(h, length):
            j = i - h
            pick = for_sort[i]
            while j >= 0: # the queue whose step is h
                if pick < for_sort[j]:
                    for_sort[j + h] = for_sort[j]   # move for vacancy
                else:
                    break
                j -= h
            for_sort[j + h] = pick # insert
        h = h // 3
    return for_sort



def merge_sort(for_sort):
    def merge(left, right):
        sorted = []
        i, j = 0, 0
        while i <= (len(left) - 1) and j <= (len(right) - 1):
            if left[i] < right[j]:
                sorted.append(left[i])
                i += 1
            else:
                sorted.append(right[j])
                j += 1
        sorted += left[i:]
        sorted += right[j:]
        return sorted
    length = len(for_sort)
    mid = length // 2
    if length <= 1:
        return for_sort
    left = merge_sort(for_sort[:mid])
    right = merge_sort(for_sort[mid:])
    return merge(left,right)


def heap_sort(for_sort):

    def heapify_shift_up(heap, i, length):
        max = i
        child_left = 2 * i + 1
        child_right = 2 * i + 2
        if child_left < length and heap[child_left] > heap[max]:
            max = child_left
        if child_right < length and heap[child_right] > heap[max]:
            max = child_right
        if max != i:
            heap[i], heap[max] = heap[max], heap[i]
            heapify_shift_up(heap, max, length)
        return None

    length = len(for_sort)
    for i in range(length // 2 - 1, -1, -1):
        heapify_shift_up(for_sort, i, length)

    while length > 1:
        for_sort[length - 1], for_sort[0] = for_sort[0],  for_sort[length - 1]
        length -= 1
        heapify_shift_up(for_sort, 0, length)
    return for_sort






def quick_sort(for_sort):
    left = 0
    right = len(for_sort) - 1

    def partition(for_sort, left, right):
        pivot = for_sort[right]
        pivot_position = left
        for i in range(left, right):
            if for_sort[i] < pivot:
                for_sort[i], for_sort[pivot_position] = for_sort[pivot_position], for_sort[i]
                pivot_position += 1
        for_sort[pivot_position], for_sort[right] = pivot, for_sort[pivot_position]
        return pivot_position

    def sort(for_sort, left, right):
        if left >= right:
            return
        last_pivot = partition(for_sort, left, right)
        sort(for_sort, left, last_pivot - 1)
        sort(for_sort, last_pivot + 1, right)

    sort(for_sort, left, right)
    return for_sort


a = [3, 2, 1]
b = [1, 2, 3, 4, 5]
test = [5, 2, 9, 4, 7, 6, 1, 3, 8]
c = a + b
print('A:{a}\nB:{b}\nA+B:{c}'.format(a = a, b = b, c = c))
print(quick_sort(c))
intersection_union(quick_sort(c))

