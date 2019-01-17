class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def recursion_core(element, start):
            if start == len(element):
                comb.append(element[:])
            else:
                for i in range(start, len(element)):
                    element[i], element[start] = element[start], element[i]
                    recursion_core(element, start + 1)
                    element[i], element[start] = element[start], element[i]
        comb = []
        recursion_core(nums, 0)
        return comb

    def permute_2(self, nums):
        """
          :type nums: List[int]
          :rtype: List[List[int]]
          """

        def recursion_core(pre_s, string):
            if not string:
                ans.append(pre_s)
                return
            for s in range(len(string)):
                recursion_core(pre_s + [string[s]], string[:s] + string[s + 1:])

        ans = []
        recursion_core([], nums)
        return ans