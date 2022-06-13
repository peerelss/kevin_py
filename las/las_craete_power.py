'''
生成维修前电压（20-38），维修后电压（39-42）
'''

import random

for i in range(1, 133):
    print(str(round(18 + random.uniform(0, 1) *20, 1)))
