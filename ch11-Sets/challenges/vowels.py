def count_vowels(text):
    vcount = 0
    vowels = set()
    vowels_check = ["a","A","e","E","i","I","o","O","u","U"] 
    for v in text:
        if v in vowels_check:
            vcount += 1
            vowels.add(v)
    return vcount,vowels
