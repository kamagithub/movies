from itertools import izip

def group(l, n = 2):
    return izip(*[iter(l)]*n)

# l = [1,2,3,4,5]
# for x, y, z in group(l,3):
#     print x, y, z