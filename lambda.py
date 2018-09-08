# a = 1 # 0001
# b = 2 # 0010
# print(a, b)
# c = a ^ b # 0011
# a = c ^ a #
# b = c ^ a
# # b = a ^ b
# print(a, b)

def multipliers():
    return [lambda x, i=i: i*x for i in range(4)]

print ([m(2) for m in multipliers()] )
"""
[0, 2, 4, 6]
"""
