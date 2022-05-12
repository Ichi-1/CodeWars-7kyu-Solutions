def flatten_and_sort(array):
    l = []
    for x in array:
        if type(x) is list:
            for elem in x:
                l.append(elem)
    return sorted(l)