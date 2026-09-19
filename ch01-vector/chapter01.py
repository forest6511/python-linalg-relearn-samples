"""第1章 矢印を数で書く
『Pythonで学び直す線形代数』サンプルコード。
Google Colab にこのファイルの内容を貼り付けて実行できます。
収録 LESSON: LESSON 01, LESSON 02, LESSON 03, LESSON 04
"""

# --- 共通の準備(序章のフォント設定セル相当) ---
# Colab では 1 回だけ実行すれば OK。日本語ラベルの豆腐(□)化を防ぐ。
!pip install -q matplotlib-fontja
import matplotlib_fontja  # noqa: F401
import numpy as np
import matplotlib.pyplot as plt


# ===== LESSON 01 矢印を、2つの数で書く =====

v = np.array([3, 2])
print(v)

v = np.array([3, 2])

plt.quiver(0, 0, v[0], v[1], angles="xy",
           scale_units="xy", scale=1, color="tab:blue")
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.gca().set_aspect("equal")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("矢印を1本描く")
plt.show()

v = np.array([3, 2])
print(v.shape)
col = np.array([[3], [2]])
print(col.shape)
print(col)

# ===== LESSON 02 矢印を足す、伸ばす、逆向きにする =====

v = np.array([3, 2])
w = np.array([1, 4])
print(v + w)

v = np.array([3, 2])
print(2 * v)
print(0.5 * v)
print(-1 * v)

# ===== LESSON 03 矢印の長さを測る =====

v = np.array([3, 2])
print(np.linalg.norm(v))

print(np.sqrt(3**2 + 2**2))

v = np.array([3, 2])
e = v / np.linalg.norm(v)
print(e)
print(np.linalg.norm(e))

u3 = np.array([1, 2, 3])
print(np.linalg.norm(u3))
u4 = np.array([1, 2, 3, 4])
print(np.linalg.norm(u4))

print(np.sqrt(1 + 4 + 9 + 16))

# ===== LESSON 04 2本の矢印を混ぜると、どこまで届くか =====

v = np.array([3, 2])
w = np.array([1, 4])
print(2 * v + 1 * w)

rng = np.random.default_rng(42)
v = np.array([3, 2])
w = np.array([1, 4])

c = rng.uniform(-1, 1, size=(100, 2))
reach = c[:, 0:1] * v + c[:, 1:2] * w

print(reach.shape)
print(np.round(reach[:3], 2))

plt.scatter(reach[:, 0], reach[:, 1], s=26,
            color="tab:gray", alpha=0.75)
plt.quiver(0, 0, v[0], v[1], angles="xy", scale_units="xy",
           scale=1, color="tab:blue")
plt.quiver(0, 0, w[0], w[1], angles="xy", scale_units="xy",
           scale=1, color="tab:orange")
plt.xlim(-10, 10)
plt.ylim(-8, 8)
plt.gca().set_aspect("equal")
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("向きが違う2本")
plt.show()

rng = np.random.default_rng(42)
v = np.array([3, 2])
w = np.array([6, 4])

c = rng.uniform(-1, 1, size=(100, 2))
reach = c[:, 0:1] * v + c[:, 1:2] * w

print(np.round(reach[:3], 2))

