def find_max(nums):
    max_so_far = float("-inf")
    for i in nums:
        if max_so_far < i:
            max_so_far = i
    return max_so_far
