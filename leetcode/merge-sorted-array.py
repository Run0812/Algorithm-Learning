def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    i = j = 0
    while j < n:
        if nums1[i] <= nums2[j]:
            if i >= m+j and nums1[i] == 0:
                nums1[i:] = nums2[j:]
                break
            i += 1
        else:
            ins_len = 0
            while j + ins_len < n and nums1[i] >= nums2[j + ins_len]:
                ins_len += 1
            nums1[i+ins_len:] = nums1[i:-ins_len]
            nums1[i:i+ins_len] = nums2[j:j + ins_len]
            j += ins_len
            i += ins_len
    return

nums1 = [-1,0,0,0,3,0,0,0,0,0,0]
m = 5
nums2 = [-1,-1,0,0,1,2]
n = 6
merge(nums1,m,nums2,n)
print(nums1)