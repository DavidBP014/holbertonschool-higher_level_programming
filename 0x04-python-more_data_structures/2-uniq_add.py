#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    uniq = list(set(my_list))
    for x in uniq:
        sum += x
    return (sum)
