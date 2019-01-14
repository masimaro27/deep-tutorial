import numpy as np
def AND(x1, x2):
    x = np.array([x1, x2])        # 입력
    w = np.array([0.5, 0.5])    # 가중치
    b = -0.7                   # 편향 (bias)
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    elif tmp > 0:
        return 1

print(AND(0,0))
print(AND(1,0))
print(AND(0,1))
print(AND(1,1))