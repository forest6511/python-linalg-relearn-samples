"""第10章 いちばん簡単な形にする（対角化）
『Pythonで学び直す線形代数』サンプルコード。
Google Colab にこのファイルの内容を貼り付けて実行できます。
収録 LESSON: LESSON 36, LESSON 37, LESSON 38, LESSON 39
"""

# --- 共通の準備(序章のフォント設定セル相当) ---
# Colab では 1 回だけ実行すれば OK。日本語ラベルの豆腐(□)化を防ぐ。
!pip install -q matplotlib-fontja
import matplotlib_fontja  # noqa: F401
import numpy as np
import matplotlib.pyplot as plt


# ===== LESSON 36 100回かけるのは大変か =====

A = np.array([[2.0, 1.0], [1.0, 2.0]])
X = np.eye(2)
for _ in range(100):
    X = A @ X
print(np.round(X, 3))

D = np.diag([2.0, 3.0])
print(D)
print(np.diag([2.0**100, 3.0**100]))
print(np.allclose(np.linalg.matrix_power(D, 100),
                  np.diag([2.0**100, 3.0**100])))

for v in [np.array([1.0, 0.0]), np.array([0.0, 1.0]),
          np.array([1.0, 1.0])]:
    print(f"{v} → {D @ v}")

Y = np.eye(2)
for _ in range(100):
    Y = D @ Y
print(np.allclose(Y, np.diag([2.0**100, 3.0**100])))
print(f"{Y[0, 0]:.6e}  {Y[1, 1]:.6e}")

# ===== LESSON 37 ものさしを取り替える =====

koyuchi, koyuvec = np.linalg.eig(A)
print(np.round(koyuchi.real, 6))
print(np.round(koyuvec.real, 4))

P = np.array([[1.0, 1.0], [1.0, -1.0]])
P_inv = np.linalg.inv(P)
print(P)
print(P_inv)

print(np.round(P_inv @ A @ P, 6))

v = np.array([3.0, 1.0])
step1 = P_inv @ v
step2 = np.diag([3.0, 1.0]) @ step1
step3 = P @ step2
print(f"もとの矢印            {v}")
print(f"ものさしを取り替える  {step1}")
print(f"3倍と1倍にする        {step2}")
print(f"もとのものさしに戻す  {step3}")
print(f"A @ v                 {A @ v}")

P2 = np.array([[1.0, 1.0], [-1.0, 1.0]])
print(np.round(np.linalg.inv(P2) @ A @ P2, 6))

# ===== LESSON 38 100乗をまとめて求める =====

lam = np.array([3.0, 1.0])
kekka1 = np.linalg.matrix_power(A, 100)
kekka2 = P @ np.diag(lam**100) @ P_inv
print(f"{kekka1[0, 0]:.6e}")
print(f"{kekka2[0, 0]:.6e}")
print(np.allclose(kekka1, kekka2))

import time
t0 = time.perf_counter()
for _ in range(10000):
    np.linalg.matrix_power(A, 100)
t1 = time.perf_counter()
for _ in range(10000):
    P @ np.diag(lam**100) @ P_inv
t2 = time.perf_counter()
print(f"matrix_power  {(t1 - t0) * 1000:5.0f} ms")
print(f"対角化を使う  {(t2 - t1) * 1000:5.0f} ms")

print((3**100 + 1) // 2)
print((3**100 - 1) // 2)
seikaku = (3**100 + 1) // 2
print(len(str(seikaku)))

Ai = np.array([[2, 1], [1, 2]], dtype=object)
Xi = np.eye(2, dtype=object)
for _ in range(100):
    Xi = Ai @ Xi
print(Xi[0, 0])
print(Xi[0, 0] == seikaku)

print(f"{kekka1[0, 0]:.0f}")
print(seikaku)
print(f"差 {abs(seikaku - int(kekka1[0, 0])):.4e}")
print(f"{2.0**53:.0f}")

Z = np.eye(2)
for _ in range(1000):
    Z = A @ Z
print(Z[0, 0])
print(len(str((3**1000 + 1) // 2)))

# ===== LESSON 39 対角化できない行列 =====

M = np.array([[0.9, 0.2], [0.1, 0.8]])
mc, mv = np.linalg.eig(M)
print(np.round(mc.real, 6))
print(np.round(mv.real, 4))

Pm = mv.real
Pm_inv = np.linalg.inv(Pm)
print(f"0.7**100 = {0.7**100:.4e}")
print(np.round(Pm @ np.diag(mc.real**100) @ Pm_inv, 6))

for hajime in [np.array([1000.0, 0.0]), np.array([0.0, 1000.0]),
               np.array([500.0, 500.0])]:
    saki = Pm @ np.diag(mc.real**100) @ Pm_inv @ hajime
    print(f"{hajime} → {np.round(saki, 4)}")

S = np.array([[1.0, 1.0], [0.0, 1.0]])
sc, sv = np.linalg.eig(S)
print(np.round(sc.real, 6))
print(np.round(sv.real, 6))
print(np.linalg.matrix_rank(sv.real))

print(f"{np.linalg.det(sv.real):.4e}")
print(np.round(np.linalg.inv(sv.real), 4))

Ps = sv.real
Ps_inv = np.linalg.inv(Ps)
Ds = Ps_inv @ S @ Ps
print(np.round(Ds, 4))
print(Ds[0, 1])
print(np.round(Ps @ Ds @ Ps_inv, 4))

def taikakuka_dekiru(X):
    koyuchi, koyuvec = np.linalg.eig(X)
    if np.any(np.abs(koyuchi.imag) > 1e-12):
        return False
    return np.linalg.matrix_rank(koyuvec.real) == X.shape[0]


for namae, X in [("A = [[2,1],[1,2]]", A),
                 ("せん断 [[1,1],[0,1]]", S),
                 ("90度回転", np.array([[0.0, -1.0], [1.0, 0.0]])),
                 ("対角 diag(2,3)", np.diag([2.0, 3.0]))]:
    print(f"{namae:22s} → {taikakuka_dekiru(X)}")

rng = np.random.default_rng(42)
kazu = 0
for _ in range(1000):
    R = rng.normal(size=(5, 5))
    if taikakuka_dekiru(R + R.T):
        kazu += 1
print(f"対角化できた対称行列 {kazu} / 1000")

Sym = np.array([[4.0, 1.0, 0.0], [1.0, 3.0, 1.0], [0.0, 1.0, 2.0]])
_, q = np.linalg.eigh(Sym)
print(np.round(q.T @ q, 10))

B = np.array([[4.0, 1.0, 0.0], [2.0, 3.0, 1.0], [0.0, 5.0, 2.0]])
_, qb = np.linalg.eig(B)
print(np.round(qb.real.T @ qb.real, 4))

