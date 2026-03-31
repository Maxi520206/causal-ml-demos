import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


np.random.seed(42)

n = 200
X = np.random.randn(n, 2)

# 拉伸不同维度
X[:, 0] *= 3.0
X[:, 1] *= 0.8


theta = np.deg2rad(35)
R = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

X = X @ R.T
