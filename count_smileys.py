def count_smileys(arr):
    count = 0
    for smile in arr:
        add = True
        if len(smile) == 2:
            if smile[0] != ':' and smile[0]!=';':
                add = False
            if smile[1] != ')' and smile[1]!='D':
                add = False
        if len(smile) == 3:
            if smile[0] != ':' and smile[0]!=';':
                add = False
            if smile[1] != '-' and smile[1]!='~':
                add = False
            if smile[2] != ')' and smile[2]!='D':
                add = False
        if add:
            count +=1
    return count