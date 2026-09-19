"""第4章 連立方程式を解く
『Pythonで学び直す線形代数』サンプルコード。
Google Colab にこのファイルの内容を貼り付けて実行できます。
収録 LESSON: LESSON 13, LESSON 14, LESSON 15, LESSON 16
"""

# --- 共通の準備(序章のフォント設定セル相当) ---
# Colab では 1 回だけ実行すれば OK。日本語ラベルの豆腐(□)化を防ぐ。
!pip install -q matplotlib-fontja
import matplotlib_fontja  # noqa: F401
import numpy as np
import matplotlib.pyplot as plt


# ===== LESSON 13 連立方程式を、行列で書き直す =====

A = np.array([[2.0, 1.0], [1.0, 1.0]])
b = np.array([4.0, 3.0])
x = np.array([1.0, 2.0])

print(A @ x)
print(np.allclose(A @ x, b))

e1 = np.array([1.0, 0.0])
e2 = np.array([0.0, 1.0])

print(A @ e1)
print(A @ e2)
print(1 * (A @ e1) + 2 * (A @ e2))

print(np.linalg.solve(A, b))

# ===== LESSON 14 解き方を、自分の手で書く =====

M = np.array([[2.0, 1.0, 4.0], [1.0, 1.0, 3.0]])

M[0] = M[0] / M[0][0]       # 1行目の左を 1 に
print(M)
M[1] = M[1] - M[1][0] * M[0]  # 2行目の左を 0 に
print(M)

M[1] = M[1] / M[1][1]       # 2行目の右を 1 に
print(M)
M[0] = M[0] - M[0][1] * M[1]  # 1行目の右を 0 に
print(M)

def hakidashi(A, b):
    """掃き出し法で A x = b を解く（行の入れ替えはしない）"""
    n = len(b)
    M = np.hstack([A.astype(float), b.reshape(n, 1).astype(float)])
    for i in range(n):                    # 何列目を片づけるか
        M[i] = M[i] / M[i][i]             # 対角を 1 にする
        for j in range(n):                # 他の行から消す
            if j != i:
                M[j] = M[j] - M[j][i] * M[i]
    return M[:, n]                        # 右端の列が答え


A = np.array([[2.0, 1.0], [1.0, 1.0]])
b = np.array([4.0, 3.0])
print(hakidashi(A, b))
print(np.allclose(hakidashi(A, b), np.linalg.solve(A, b)))

A3 = np.array([[2.0, 1.0, -1.0],
               [1.0, 3.0, 2.0],
               [1.0, 1.0, 1.0]])
b3 = np.array([3.0, 13.0, 6.0])
print(hakidashi(A3, b3))
print(np.linalg.solve(A3, b3))

# ===== LESSON 15 解けないときが、ある =====

C = np.array([[1.0, 2.0], [2.0, 4.0]])
print(C @ np.array([1.0, 0.0]))
print(C @ np.array([0.0, 1.0]))

try:
    np.linalg.solve(C, np.array([1.0, 3.0]))
except np.linalg.LinAlgError as e:
    print("LinAlgError:", e)

try:
    np.linalg.solve(C, np.array([1.0, 2.0]))
except np.linalg.LinAlgError as e:
    print("LinAlgError:", e)

for t in [0.0, 1.0, 2.0, -3.0]:
    x = np.array([1.0 - 2.0 * t, t])
    print(t, C @ x)

ans, *_ = np.linalg.lstsq(C, np.array([1.0, 2.0]), rcond=None)
print(np.round(ans, 3))
print(np.allclose(C @ ans, np.array([1.0, 2.0])))

# ===== LESSON 16 行を入れ替える理由 =====

Ap = np.array([[1e-17, 1.0], [1.0, 1.0]])
bp = np.array([1.0, 2.0])

print(hakidashi(Ap, bp))
print(np.linalg.solve(Ap, bp))

M = np.hstack([Ap.copy(), bp.reshape(2, 1)])
M[0] = M[0] / M[0][0]
print(M)
M[1] = M[1] - M[1][0] * M[0]
print(M)

Ap2 = np.array([[1.0, 1.0], [1e-17, 1.0]])
bp2 = np.array([2.0, 1.0])
print(hakidashi(Ap2, bp2))

import time

rng = np.random.default_rng(42)
for n in [10, 100, 500]:
    A = rng.random((n, n)) + n * np.eye(n)
    b = rng.random(n)
    start = time.time()
    np.linalg.solve(A, b)
    print(f"{n} 元連立: {(time.time() - start) * 1000:.1f} ミリ秒")

