'''
___G
__GG
_GGG
GGGG
'''

g = 1
for i in range(5, 1, -1):
    for j in range(i, 2, -1):
        print(" ", end="")
    for k in range(0, g):
        print("G", end="")
    print()
    g = g + 1


