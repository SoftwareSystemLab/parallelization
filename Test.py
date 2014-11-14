# -*- coding: utf-8 -*-
'''
Created on 2014/5/22
@author: Ivy Liu
'''

import time, itertools

# 記錄開始時間 Record start time
tStart = time.time()

# 跑一個permutation
for item in (itertools.permutations("0123456789", 6)):
    print(''.join(item))

# 記錄結束時間 Record stop time
tStop = time.time()

print(tStop - tStart)