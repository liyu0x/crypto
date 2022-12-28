import numpy as np
import present

BCT = np.zeros((16, 16), dtype=int)

for i in range(16):
    for j in range(16):
        for n in range(16):
            out = present.S_BOX_REV[present.S_BOX[n] ^ j] ^ present.S_BOX_REV[
                present.S_BOX[n ^ i] ^ j]
            if out == i:
                BCT[i][j] += 1
