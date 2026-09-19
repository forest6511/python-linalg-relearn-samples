"""第6章 つぶれたかを数で判定する（行列式）
『Pythonで学び直す線形代数』サンプルコード。
Google Colab にこのファイルの内容を貼り付けて実行できます。
収録 LESSON: LESSON 21, LESSON 22, LESSON 23, LESSON 24
"""

# --- 共通の準備(序章のフォント設定セル相当) ---
# Colab では 1 回だけ実行すれば OK。日本語ラベルの豆腐(□)化を防ぐ。
!pip install -q matplotlib-fontja
import matplotlib_fontja  # noqa: F401
import numpy as np
import matplotlib.pyplot as plt


# ===== LESSON 21 つぶれたかを数だけで判定する =====

A = np.array([[3.0, 1.0], [1.0, 2.0]])
e1 = np.array([1.0, 0.0])
e2 = np.array([0.0, 1.0])

print(A @ e1)
print(A @ e2)

def menseki(A):
    """2行2列の行列が作る平行四辺形の面積のもと"""
    a, b = A[0][0], A[0][1]
    c, d = A[1][0], A[1][1]
    return a * d - b * c


print(menseki(A))

print(np.linalg.det(A))

C = np.array([[1.0, 2.0], [2.0, 4.0]])
print(menseki(C))
print(np.linalg.det(C))

for y in [2.0, 1.6, 1.2, 1.0]:
    M = np.array([[1.0, 1.0], [1.0, y]])
    print(f"y={y}  det={np.linalg.det(M):.1f}")

# ===== LESSON 22 面積が負になる =====

B = np.array([[1.0, 2.0], [3.0, 1.0]])
print(np.linalg.det(B))
print(abs(np.linalg.det(B)))

K = np.array([[0.0, 1.0], [1.0, 0.0]])
print(np.linalg.det(K))

for kakudo in [0, 30, 90, 137, 270]:
    t = np.radians(kakudo)
    R = np.array([[np.cos(t), -np.sin(t)],
                  [np.sin(t), np.cos(t)]])
    print(f"{kakudo}度  det={np.linalg.det(R):.10f}")

D = np.array([[0.1, 0.2], [0.3, 0.6]])
print(np.linalg.det(D))
print(np.linalg.det(D) == 0)
print(np.isclose(np.linalg.det(D), 0))

# ===== LESSON 23 3行3列の行列式を作る =====

A3 = np.array([[2.0, 1.0, -1.0],
               [1.0, 3.0, 2.0],
               [1.0, 1.0, 1.0]])


def sarrus(A):
    """3行3列だけで使える行列式の求め方"""
    a, b, c = A[0]
    d, e, f = A[1]
    g, h, i = A[2]
    return a * e * i + b * f * g + c * d * h \
        - c * e * g - a * f * h - b * d * i


print(sarrus(A3))
print(np.linalg.det(A3))

P = np.array([[2.0, 1.0], [1.0, 1.0]])
Q = np.array([[0.0, -1.0], [1.0, 0.0]])

print(np.linalg.det(P @ Q))
print(np.linalg.det(P) * np.linalg.det(Q))

rng = np.random.default_rng(42)
A4 = rng.integers(-3, 4, size=(4, 4)).astype(float)

print(A4)
print(np.linalg.det(A4))

# ===== LESSON 24 教科書の方法では計算できない =====

def det_saiki(A):
    """余因子展開を使って、どんな大きさでも行列式を出す"""
    n = len(A)
    if n == 1:                        # 1行1列ならその数そのもの
        return A[0][0]
    goukei = 0.0
    for j in range(n):                # 1行目の各列を順に選ぶ
        chiisai = np.delete(np.delete(A, 0, axis=0), j, axis=1)
        fugou = (-1) ** j             # 符号が1つおきに入れ替わる
        goukei += fugou * A[0][j] * det_saiki(chiisai)
    return goukei


print(det_saiki(A3))
print(det_saiki(A4))
print(np.isclose(det_saiki(A4), np.linalg.det(A4)))

import time

for n in [5, 6, 7, 8, 9]:
    M = rng.random((n, n))
    start = time.time()
    det_saiki(M)
    print(f"{n}x{n}  {(time.time() - start) * 1000:8.1f} ミリ秒")

import math

for n in [5, 10, 20, 30]:
    print(f"{n}x{n}  約 {math.factorial(n):.1e} 回")

M20 = rng.random((20, 20))
start = time.time()
np.linalg.det(M20)
print(f"20x20: {(time.time() - start) * 1000:.3f} ミリ秒")

