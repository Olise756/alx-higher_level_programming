#!/usr/bin/python3
my_list = [1,2,3,4,5]

def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        print("the element at {} is {} ".format(idx, my_list[idx]))
element_at(my_list, 3)
