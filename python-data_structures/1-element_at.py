#!/udr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return "None"
    elif idx > len(my_list):
        return "None"
    else:
        for i, n in enumerate(my_list):
            if idx == i:
                return n
