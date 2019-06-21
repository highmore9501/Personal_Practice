L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    name = t[0]
    return name
    pass

def by_score(t):
    score = t[1]
    return score
    pass

L2 = sorted(L, key=by_score)
print(L2)

L2 = sorted(L, key=by_name)
print(L2)
