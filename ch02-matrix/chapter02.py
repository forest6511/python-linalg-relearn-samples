"""第2章 行列は変形の機械
『Pythonで学び直す線形代数』サンプルコード。
Google Colab にこのファイルの内容を貼り付けて実行できます。
収録 LESSON: LESSON 06, LESSON 07, LESSON 08
"""

# --- 共通の準備(序章のフォント設定セル相当) ---
# Colab では 1 回だけ実行すれば OK。日本語ラベルの豆腐(□)化を防ぐ。
!pip install -q matplotlib-fontja
import matplotlib_fontja  # noqa: F401
import numpy as np
import matplotlib.pyplot as plt


# ===== LESSON 06 行き先を2本だけ書き留める =====

e1_go = np.array([2, 1])   # 横に真っ直ぐの矢印の行き先
e2_go = np.array([1, 1])   # 縦に真っ直ぐの矢印の行き先

A = np.array([[2, 1], [1, 1]])
print(A)

print(A[:, 0])
print(A[:, 1])

v = np.array([1, 2])
print(v[0] * A[:, 0] + v[1] * A[:, 1])

# ===== LESSON 07 掛け算を、自分の手で書く =====

def matvec(A, v):
    """行列 A で矢印 v を動かす（numpy の @ を使わずに書く）"""
    kekka = [0, 0]
    for i in range(2):          # 答えの何番目を作るか
        for j in range(2):      # 元の矢印の何番目を使うか
            kekka[i] = kekka[i] + A[i][j] * v[j]
    return np.array(kekka)


A = np.array([[2, 1], [1, 1]])
v = np.array([1, 2])
print(matvec(A, v))

print(A @ v)
print(np.allclose(matvec(A, v), A @ v))

print(np.dot(A, v))
print(np.matmul(A, v))

print(A.shape)
B = np.array([[1, 0], [0, 1], [1, 1]])
print(B.shape)
print(B @ v)

R = np.array([[0, -1], [1, 0]])
v = np.array([1, 2])
print(R @ v)

# ===== LESSON 08 4つの変形を見分ける =====

katachi = {
    "伸ばす": np.array([[2, 0], [0, 1]]),
    "回す": np.array([[0, -1], [1, 0]]),
    "倒す": np.array([[1, 1], [0, 1]]),
    "つぶす": np.array([[1, 2], [2, 4]]),
}

v = np.array([1, 1])
for namae, M in katachi.items():
    print(namae, M @ v)

rng = np.random.default_rng(42)
C = np.array([[1, 2], [2, 4]])

kaku = rng.uniform(0, 2 * np.pi, 100)
moto = np.stack([np.cos(kaku), np.sin(kaku)])
saki = C @ moto

print(np.round(saki[:, :3], 2))

print(np.round(saki[1] / saki[0], 4)[:5])

