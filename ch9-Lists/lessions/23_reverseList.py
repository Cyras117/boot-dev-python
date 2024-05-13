def reverse_array(items):
    ret = []
    for i in range(len(items)-1,-1,-1):
        ret.append(items[i])
    return ret