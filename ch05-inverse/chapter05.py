"""第5章 元に戻せる変形、戻せない変形（逆行列）
『Pythonで学び直す線形代数』サンプルコード。
Google Colab にこのファイルの内容を貼り付けて実行できます。
収録 LESSON: LESSON 17, LESSON 18, LESSON 19, LESSON 20
"""

# --- 共通の準備(序章のフォント設定セル相当) ---
# Colab では 1 回だけ実行すれば OK。日本語ラベルの豆腐(□)化を防ぐ。
!pip install -q matplotlib-fontja
import matplotlib_fontja  # noqa: F401
import numpy as np
import matplotlib.pyplot as plt


# ===== LESSON 17 元に戻す変形を探す =====

A = np.array([[2.0, 1.0], [1.0, 1.0]])
B = np.array([[1.0, -1.0], [-1.0, 2.0]])

print(A @ B)
print(np.allclose(A @ B, np.eye(2)))
print(np.allclose(B @ A, np.eye(2)))

v = np.array([3.0, 1.0])
print(A @ v)
print(B @ (A @ v))

print(np.linalg.inv(A))
print(np.allclose(np.linalg.inv(A), B))

def inv2(A):
    """2行2列の逆行列を公式で作る"""
    a, b = A[0][0], A[0][1]
    c, d = A[1][0], A[1][1]
    shihai = a * d - b * c          # 戻せるかを決める数
    return np.array([[d, -b], [-c, a]]) / shihai


print(inv2(A))
print(np.allclose(inv2(A), np.linalg.inv(A)))

# ===== LESSON 18 戻せない変形がある =====

C = np.array([[1.0, 2.0], [2.0, 4.0]])
print(C @ np.array([1.0, 0.0]))
print(C @ np.array([-1.0, 1.0]))

try:
    np.linalg.inv(C)
except np.linalg.LinAlgError as e:
    print("LinAlgError:", e)

for y in [2.0, 1.5, 1.2, 1.05, 1.001]:
    M = np.array([[1.0, 1.0], [1.0, y]])
    print(f"y={y}  inv の左上={np.linalg.inv(M)[0][0]:.1f}")

for y in [2.0, 1.5, 1.2, 1.05, 1.001]:
    M = np.array([[1.0, 1.0], [1.0, y]])
    print(f"y={y}  cond={np.linalg.cond(M):.1f}")

# ===== LESSON 19 逆行列で連立方程式を解かない =====

A = np.array([[2.0, 1.0], [1.0, 1.0]])
b = np.array([4.0, 3.0])

print(np.linalg.inv(A) @ b)
print(np.linalg.solve(A, b))

def hilbert(n):
    """つぶれかけた行列の代表例を作る"""
    return np.array([[1.0 / (i + j + 1) for j in range(n)]
                     for i in range(n)])


H = hilbert(12)
kotae = np.ones(12)
b12 = H @ kotae

print(np.max(np.abs(np.linalg.inv(H) @ b12 - kotae)))
print(np.max(np.abs(np.linalg.solve(H, b12) - kotae)))

import time

rng = np.random.default_rng(42)
n = 500
An = rng.random((n, n)) + n * np.eye(n)
bn = rng.random(n)
np.linalg.solve(An, bn)  # 準備

start = time.time()
np.linalg.inv(An) @ bn
print(f"inv で解く  : {(time.time() - start) * 1000:.1f} ミリ秒")

start = time.time()
np.linalg.solve(An, bn)
print(f"solve で解く: {(time.time() - start) * 1000:.1f} ミリ秒")

# ===== LESSON 20 転置と逆行列を取り違えない =====

A = np.array([[2.0, 1.0], [1.0, 1.0]])
print(A.T)
print(np.allclose(A.T, np.linalg.inv(A)))

R = np.array([[0.0, -1.0], [1.0, 0.0]])
print(R.T)
print(np.allclose(R.T, np.linalg.inv(R)))
print(R.T @ R)

for kakudo in [30, 45, 137]:
    t = np.radians(kakudo)
    Rt = np.array([[np.cos(t), -np.sin(t)],
                   [np.sin(t), np.cos(t)]])
    print(kakudo, np.allclose(Rt.T, np.linalg.inv(Rt)))

A3 = np.array([[2.0, 1.0, -1.0],
               [1.0, 3.0, 2.0],
               [1.0, 1.0, 1.0]])
print(np.round(np.linalg.inv(A3), 3))
print(np.allclose(A3 @ np.linalg.inv(A3), np.eye(3)))

