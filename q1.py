
# ******************************
# Make your Code
# ******************************
cn = 0
pn = 0
i = 0
c = 0
while i < 10:
    n = int(input())
    cn = n
    if cn % 2 == 0 and pn % 2 == 0 and cn != 0 and pn != 0:
        c += 1
    pn = cn
    i += 1
print(c)

# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
