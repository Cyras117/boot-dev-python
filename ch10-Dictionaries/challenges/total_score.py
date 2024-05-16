def merge(dict1, dict2):
    mdict = {}
    for item in dict1:
        mdict[item] = dict1[item]
    for item in dict2:
        mdict[item] = dict2[item]
    return mdict

def total_score(score_dict):
    total = 0
    for score in score_dict:
        total += score_dict[score]
    return total