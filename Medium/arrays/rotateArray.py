class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        temp = []

        if k == 0:
            return None
        if len(nums) == 1 : 
            return None
        if k > len(nums):
            k = k % len(nums)
        for i in range(len(nums)-k,len(nums)):
            nums.append(nums[i])
        print("first version: " + str(nums))
        for i in range(len(nums)-k,k-1,-1):
            nums[i] = nums[i-k]
        print("second version: " + str(nums))
        for i in range(k):
            nums[i] = nums[i+len(nums)-k]
        print("third version: " + str(nums))
        for i in range(k):
            nums.pop()
        return None
        
    def rotate(self, nums, k):
        def reverse(array, start,end):
            while start < end : 
                array[start], array[end] = array[end], array[start]
                start += 1
                end -= 1

        if k > len(nums):
            k = k%len(nums)
        
        reverse(nums, 0, len(nums)-1)

        reverse(nums, 0, k-1)
        
        reverse(nums, k, len(nums)-1)

        return None

