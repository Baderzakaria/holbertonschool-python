def add_tuple(my_string):
    i=0
    for c in my_string:
        if c=='c' or c=='C':
            my_string.pop(i)
        i+=1
    return my_string