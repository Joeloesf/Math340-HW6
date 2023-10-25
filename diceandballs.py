"""
author: Joseph Loeffler
"""

import random

trials = 1000000

XTot = 0
AbigailTot = 0

AbigailWins = 0

dic = {}

for _ in range(trials):
    X = 0
    Abigail = 0

    while True:
        if random.choice([1,2,3,4,5,6]) < 3:
            AbigailWins += 1
            if X == 0:
                Abigail += 10
            else:
                Abigail += 5
            break
        else:
            X += 1
            if random.choice([0,1]) == 1:  # 1 is for heads
                break
    
    XTot += X
    AbigailTot += Abigail

    if X not in dic.keys():
        dic[X] = 0
    dic[X] += 1

### print probs of X ###
# for key, value in dic.items():
#     print("P(" + str(key) + ") = " + str(value/trials))
#     if key==0:
#         print("Diff(" + str(key) + ") = " + str((value/trials) - (1/3)))
#     else:
#         print("Diff(" + str(key) + ") = " + str(value/trials - ((4/9)*(1/3)**(key-1))))

### print E(X) ###
# print("E(X) = ", XTot/trials)

### print E(Abigail) ###
print("E(A) = ", AbigailTot/trials)