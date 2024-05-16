def remove_nonints(nums):
    list_return = []
    for n in nums:
        if type(n) == int:
            list_return.append(n)
    return list_return