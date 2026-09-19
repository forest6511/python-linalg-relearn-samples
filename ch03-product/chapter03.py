"""第3章 変形を続けてやる（行列の積）
『Pythonで学び直す線形代数』サンプルコード。
Google Colab にこのファイルの内容を貼り付けて実行できます。
収録 LESSON: LESSON 09, LESSON 10, LESSON 11, LESSON 12
"""

# --- 共通の準備(序章のフォント設定セル相当) ---
# Colab では 1 回だけ実行すれば OK。日本語ラベルの豆腐(□)化を防ぐ。
!pip install -q matplotlib-fontja
import matplotlib_fontja  # noqa: F401
import numpy as np
import matplotlib.pyplot as plt


# ===== LESSON 09 変形を2回続けると、どうなるか =====

R = np.array([[0, -1], [1, 0]])   # 90度回す
S = np.array([[1, 1], [0, 1]])    # 倒す（せん断）

v = np.array([1, 0])
print(S @ v)
print(R @ (S @ v))

e1 = np.array([1, 0])
e2 = np.array([0, 1])
print(R @ (S @ e1))
print(R @ (S @ e2))

RS = np.array([[0, -1], [1, 1]])
print(RS)

v = np.array([1, 0])
print(RS @ v)

print(R @ S)
print(np.allclose(R @ S, RS))

# ===== LESSON 10 積の規則を、自分で導く =====

def matmul(A, B):
    """行列 A と B の積（numpy の @ を使わずに書く）"""
    kekka = [[0, 0], [0, 0]]
    for i in range(2):              # 答えの何行目か
        for j in range(2):          # 答えの何列目か
            for k in range(2):      # 足し合わせる相手
                kekka[i][j] = kekka[i][j] + A[i][k] * B[k][j]
    return np.array(kekka)


R = np.array([[0, -1], [1, 0]])
S = np.array([[1, 1], [0, 1]])
print(matmul(R, S))
print(np.allclose(matmul(R, S), R @ S))

# ===== LESSON 11 順番を変えると、答えが変わる =====

print(R @ S)
print(S @ R)
print(np.allclose(R @ S, S @ R))

v = np.array([1, 0])
print((R @ S) @ v)
print((S @ R) @ v)

D1 = np.array([[2, 0], [0, 3]])
D2 = np.array([[5, 0], [0, 7]])
print(np.allclose(D1 @ D2, D2 @ D1))

E = np.eye(2)
print(E)
print(np.allclose(R @ E, R) and np.allclose(E @ R, R))

# ===== LESSON 12 3回以上続ける、形を合わせる =====

A = np.array([[2, 0], [0, 1]])
print((R @ S) @ A)
print(R @ (S @ A))
print(np.allclose((R @ S) @ A, R @ (S @ A)))

print(S @ S @ S)
print(np.linalg.matrix_power(S, 3))

P = np.array([[1, 2, 3], [4, 5, 6]])
Q = np.array([[1, 0], [0, 1], [1, 1]])
print(P.shape, Q.shape)
print(P @ Q)

try:
    P @ P
except ValueError as e:
    print("ValueError:", e)

A = np.array([[2, 1], [1, 1]])
B = np.array([[1, 2], [3, 4]])
print(A[0] @ B[:, 0])
print((A @ B)[0, 0])

import time

A = np.array([[2.0, 1.0], [1.0, 1.0]])
B = np.array([[1.0, 2.0], [3.0, 4.0]])

start = time.time()
for _ in range(10000):
    matmul(A, B)
print(f"自作 matmul: {time.time() - start:.3f} 秒")

start = time.time()
for _ in range(10000):
    A @ B
print(f"numpy の @ : {time.time() - start:.3f} 秒")

rng = np.random.default_rng(42)
big = rng.random((200, 200))

start = time.time()
big @ big
print(f"200x200 の積: {(time.time() - start) * 1000:.1f} ミリ秒")

