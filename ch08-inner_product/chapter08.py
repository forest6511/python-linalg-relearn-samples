"""第8章 直角と影（内積と正射影）
『Pythonで学び直す線形代数』サンプルコード。
Google Colab にこのファイルの内容を貼り付けて実行できます。
収録 LESSON: LESSON 29, LESSON 30, LESSON 31
"""

# --- 共通の準備(序章のフォント設定セル相当) ---
# Colab では 1 回だけ実行すれば OK。日本語ラベルの豆腐(□)化を防ぐ。
!pip install -q matplotlib-fontja
import matplotlib_fontja  # noqa: F401
import numpy as np
import matplotlib.pyplot as plt


# ===== LESSON 29 向きの近さを数にする =====

v = np.array([3.0, 2.0])
w = np.array([1.0, 4.0])


def naiseki(a, b):
    """掛けて足すだけ"""
    goukei = 0.0
    for i in range(len(a)):
        goukei = goukei + a[i] * b[i]
    return goukei


print(naiseki(v, w))
print(v @ w)
print(np.dot(v, w))

for kakudo in [0, 30, 60, 90, 120, 180]:
    rad = np.radians(kakudo)
    b = np.array([np.cos(rad), np.sin(rad)])
    print(f"{kakudo:3d}度  内積={np.array([1.0, 0.0]) @ b:6.3f}")

cos_theta = (v @ w) / (np.linalg.norm(v) * np.linalg.norm(w))
print(f"{cos_theta:.4f}")
print(f"{np.degrees(np.arccos(cos_theta)):.2f}")

print(np.linalg.norm(v) ** 2)
print(v @ v)
print(np.isclose(np.linalg.norm(v) ** 2, v @ v))

# ===== LESSON 30 図が描けない次元でも直角は分かる =====

p = np.array([1.0, 2.0, 2.0])
q = np.array([2.0, -2.0, 1.0])
print(p @ q)
print(np.linalg.norm(p), np.linalg.norm(q))

rng = np.random.default_rng(42)
a100 = rng.normal(size=100)
c100 = rng.normal(size=100)
c100 = c100 - (c100 @ a100) / (a100 @ a100) * a100
print(f"{a100 @ c100:.2e}")
print(np.isclose(a100 @ c100, 0))
print(a100.shape)

rng = np.random.default_rng(0)
for jigen in [2, 3, 10, 100, 1000]:
    kakudo_list = []
    for _ in range(200):
        x = rng.normal(size=jigen)
        y = rng.normal(size=jigen)
        cos_t = (x @ y) / (np.linalg.norm(x) * np.linalg.norm(y))
        kakudo_list.append(np.degrees(np.arccos(cos_t)))
    kakudo_list = np.array(kakudo_list)
    print(f"{jigen:5d}次元  平均={kakudo_list.mean():6.2f}度  "
          f"ばらつき={kakudo_list.std():5.2f}度")

d100 = c100.copy()
d100[0] = d100[0] + 1.0
print(f"{a100 @ d100:.4f}")
print(np.isclose(a100 @ d100, 0))

# ===== LESSON 31 矢印の影を落とす =====

u = np.array([4.0, 3.0])
t = np.array([1.0, 1.0])

kage_vec = (u @ t) / (t @ t) * t
print(kage_vec)
print(np.linalg.norm(kage_vec))

sa = u - kage_vec
print(sa)
print(f"{sa @ t:.2e}")
print(np.isclose(sa @ t, 0))

P = np.outer(t, t) / (t @ t)
print(P)
print(P @ u)

print(P @ (P @ u))
print(np.allclose(P @ P, P))

rng = np.random.default_rng(7)
x = np.linspace(0, 10, 12)
y = 0.8 * x + 2.0 + rng.normal(0, 1.0, size=12)
A = np.column_stack([x, np.ones(12)])
kai, *_ = np.linalg.lstsq(A, y, rcond=None)
print(np.round(kai, 4))

zansa = y - A @ kai
print(f"{zansa @ A[:, 0]:.2e}")
print(f"{zansa @ A[:, 1]:.2e}")

y2 = y.copy()
y2[5] = y2[5] + 12.0
kai2, *_ = np.linalg.lstsq(A, y2, rcond=None)
print(np.round(kai2, 4))

