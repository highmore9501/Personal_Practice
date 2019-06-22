def normalize(name):
    s = name.capitalize()
    return s
    pass

# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
