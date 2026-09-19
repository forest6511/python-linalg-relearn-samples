"""第9章 変わらない方向を探す（固有値・固有ベクトル）
『Pythonで学び直す線形代数』サンプルコード。
Google Colab にこのファイルの内容を貼り付けて実行できます。
収録 LESSON: LESSON 32, LESSON 33, LESSON 34, LESSON 35
"""

# --- 共通の準備(序章のフォント設定セル相当) ---
# Colab では 1 回だけ実行すれば OK。日本語ラベルの豆腐(□)化を防ぐ。
!pip install -q matplotlib-fontja
import matplotlib_fontja  # noqa: F401
import numpy as np
import matplotlib.pyplot as plt


# ===== LESSON 32 向きが変わらない矢印を探す =====

A = np.array([[2.0, 1.0], [1.0, 2.0]])
kakudo = np.arange(15, 360, 30)
moto = np.array([[np.cos(np.radians(k)), np.sin(np.radians(k))]
                 for k in kakudo])
saki = moto @ A.T

for k, m, s in zip(kakudo, moto, saki):
    mk = np.degrees(np.arctan2(m[1], m[0])) % 360
    sk = np.degrees(np.arctan2(s[1], s[0])) % 360
    zure = (sk - mk + 180) % 360 - 180
    print(f"{k:3d}度 → {sk:6.1f}度   向きの変化 {zure:6.1f}度")

for v in [np.array([1.0, 1.0]), np.array([1.0, -1.0])]:
    print(f"{v} → {A @ v}")

print((A @ np.array([1.0, 1.0])) / np.array([1.0, 1.0]))
print((A @ np.array([1.0, -1.0])) / np.array([1.0, -1.0]))

v = np.array([1.0, 0.9])
saki_v = A @ v
print(np.round(saki_v, 4))
print(f"{np.degrees(np.arctan2(v[1], v[0])):.2f}")
print(f"{np.degrees(np.arctan2(saki_v[1], saki_v[0])):.2f}")

# ===== LESSON 33 固有ベクトルは何の役に立つのか =====

A = np.array([[2.0, 1.0], [1.0, 2.0]])
v = np.array([1.0, 0.0])
for kai in range(6):
    kaku = np.degrees(np.arctan2(v[1], v[0]))
    print(f"{kai}回目  向き={kaku:5.1f}度  長さ={np.linalg.norm(v):8.2f}")
    v = A @ v

v = np.array([1.0, 0.0])
for kai in range(7):
    kaku = np.degrees(np.arctan2(v[1], v[0]))
    print(f"{kai}回目  向き={kaku:5.2f}度")
    v = A @ v
    v = v / np.linalg.norm(v)

print(f"{v @ (A @ v):.6f}")

M = np.array([[0.9, 0.2], [0.1, 0.8]])
jotai = np.array([1000.0, 0.0])
for tsuki in range(6):
    print(f"{tsuki:2d}か月後  A={jotai[0]:7.1f}  B={jotai[1]:7.1f}  "
          f"比={jotai[0] / jotai[1]:.3f}" if tsuki > 0 else
          f"{tsuki:2d}か月後  A={jotai[0]:7.1f}  B={jotai[1]:7.1f}")
    jotai = M @ jotai

rng = np.random.default_rng(42)
hiritsu = []
for _ in range(1000):
    x = rng.uniform(0, 1000, size=2)
    for _ in range(200):
        x = M @ x
    hiritsu.append(x[0] / x[1])
hiritsu = np.array(hiritsu)
print(f"最小={hiritsu.min():.6f}  最大={hiritsu.max():.6f}")
print(np.allclose(hiritsu, 2.0))

jotai = np.array([0.0, 1000.0])
for _ in range(200):
    jotai = M @ jotai
print(np.round(jotai, 4))
print(f"{jotai[0] / jotai[1]:.6f}")

# ===== LESSON 34 固有値を計算で求める =====

for lam in [3.0, 1.0, 2.0]:
    B = A - lam * np.eye(2)
    print(f"λ={lam}  det(A-λE)={np.linalg.det(B):6.2f}")

koyuchi, koyuvec = np.linalg.eig(A)
print(koyuchi)
print(koyuvec)

print(koyuvec[:, 0])
print(koyuvec[:, 1])
print(np.linalg.norm(koyuvec[:, 0]))

print(A @ koyuvec[:, 0])
print(koyuchi[0] * koyuvec[:, 0])
print(np.allclose(A @ koyuvec[:, 0], koyuchi[0] * koyuvec[:, 0]))

for bai in [1.0, 2.0, -3.0]:
    v = bai * np.array([1.0, 1.0])
    print(f"{bai:5.1f}倍  A@v={A @ v}  3*v={3 * v}")

R = np.array([[0.0, -1.0], [1.0, 0.0]])
kc, kv = np.linalg.eig(R)
print(kc)
print(np.round(kv, 4))

S = np.array([[1.0, 1.0], [0.0, 1.0]])
sc, sv = np.linalg.eig(S)
print(sc)
print(np.round(sv, 4))
print(np.linalg.matrix_rank(sv))

# ===== LESSON 35 大きい行列ではどうするか =====

A3 = np.array([[4.0, 1.0, 0.0], [1.0, 3.0, 1.0], [0.0, 1.0, 2.0]])
kc3, kv3 = np.linalg.eig(A3)
print(np.round(kc3, 6))

import time
rng = np.random.default_rng(0)
big = rng.normal(size=(100, 100))
big = big + big.T
t0 = time.perf_counter()
kc_big = np.linalg.eigvalsh(big)
t1 = time.perf_counter()
print(f"100x100 の固有値 {len(kc_big)} 個  {(t1 - t0) * 1000:.1f} ms")
print(f"最小={kc_big.min():.3f}  最大={kc_big.max():.3f}")

print(np.iscomplexobj(kc_big))

big2 = rng.normal(size=(100, 100))
kc_big2 = np.linalg.eig(big2)[0]
print(np.iscomplexobj(kc_big2))
print(f"複素数の固有値の個数 {int(np.sum(np.abs(kc_big2.imag) > 1e-12))}")

