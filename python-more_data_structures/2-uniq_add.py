#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    seen = set()

    for num in my_list:
        if num not in seen:
            total += num
            seen.add(num)

    return total
