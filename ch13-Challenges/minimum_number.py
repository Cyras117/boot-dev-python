def find_min(nums):
    mini = float("inf")
    for n in nums:
        if n < mini:
            mini = n
    return mini
