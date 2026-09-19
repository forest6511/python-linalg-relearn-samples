"""第7章 無駄のない組（一次独立・基底・rank）
『Pythonで学び直す線形代数』サンプルコード。
Google Colab にこのファイルの内容を貼り付けて実行できます。
収録 LESSON: LESSON 25, LESSON 26, LESSON 27, LESSON 28
"""

# --- 共通の準備(序章のフォント設定セル相当) ---
# Colab では 1 回だけ実行すれば OK。日本語ラベルの豆腐(□)化を防ぐ。
!pip install -q matplotlib-fontja
import matplotlib_fontja  # noqa: F401
import numpy as np
import matplotlib.pyplot as plt


# ===== LESSON 25 2本で届く範囲が変わる =====

rng = np.random.default_rng(42)
v1 = np.array([1.0, 0.5])
v2 = np.array([0.5, 1.5])

tenS = np.array([a * v1 + b * v2
                 for a, b in rng.uniform(-2, 2, size=(100, 2))])
print(tenS.shape)
print(np.round(tenS[:3], 2))

w1 = np.array([1.0, 2.0])
w2 = np.array([2.0, 4.0])

tenT = np.array([a * w1 + b * w2
                 for a, b in rng.uniform(-2, 2, size=(100, 2))])
print(np.round(tenT[:3], 2))
print(np.allclose(tenT[:, 1] / tenT[:, 0], 2.0))

print(2.0 * w1 - 1.0 * w2)
print(2.0 * v1 - 1.0 * v2)

# ===== LESSON 26 現象に名前を付ける =====

def yontsu_no_kao(A):
    """同じ事実を4つの言い方で確かめる"""
    d = np.linalg.det(A)
    r = np.linalg.matrix_rank(A)
    modoseru = not np.isclose(d, 0)
    print(f"  戻せるか      : {modoseru}")
    print(f"  det が 0 でない: {not np.isclose(d, 0)}  (det={d:.1f})")
    print(f"  一次独立か    : {r == len(A)}")
    print(f"  rank が最大か  : {r == len(A)}  (rank={r})")


print("V = 別々の向きの2本")
yontsu_no_kao(np.column_stack([v1, v2]))
print("W = 同じ向きの2本")
yontsu_no_kao(np.column_stack([w1, w2]))

print(np.linalg.matrix_rank(np.column_stack([v1, v2])))
print(np.linalg.matrix_rank(np.column_stack([w1, w2])))
print(np.linalg.matrix_rank(np.zeros((2, 2))))

v3 = np.array([2.0, -1.0])
print(np.linalg.matrix_rank(np.column_stack([v1, v2, v3])))

# ===== LESSON 27 ぴったりは判定できない =====

for eps in [1.0, 0.01, 1e-8, 1e-14, 1e-15, 1e-16]:
    M = np.array([[1.0, 2.0], [2.0, 4.0 + eps]])
    print(f"eps={eps:.0e}  det={np.linalg.det(M):.2e}  "
          f"rank={np.linalg.matrix_rank(M)}")

M = np.array([[1.0, 2.0], [2.0, 4.0 + 1e-8]])
print(np.linalg.matrix_rank(M))
print(np.linalg.matrix_rank(M, tol=1e-6))

u1 = np.array([1.0, 0.0, 1.0])
u2 = np.array([0.0, 1.0, 1.0])
u3 = u1 + u2

U = np.column_stack([u1, u2, u3])
print(U)
print(np.linalg.matrix_rank(U))
print(np.linalg.det(U))

u3b = np.array([0.0, 0.0, 1.0])
Ub = np.column_stack([u1, u2, u3b])
print(np.linalg.matrix_rank(Ub))
print(np.linalg.det(Ub))

# ===== LESSON 28 ものさしを取り替える =====

b1 = np.array([1.0, 1.0])
b2 = np.array([2.0, 1.0])
P = np.column_stack([b1, b2])

print(P)
print(np.linalg.matrix_rank(P))

v = np.array([3.0, 1.0])
zahyou = np.linalg.solve(P, v)
print(zahyou)

print(zahyou[0] * b1 + zahyou[1] * b2)

print(b1 @ b2)
print(v1 @ v2)
print(np.linalg.matrix_rank(np.column_stack([v1, v2])))

