"""第11章 終章 大きい行列と、この先へ
『Pythonで学び直す線形代数』サンプルコード。
Google Colab にこのファイルの内容を貼り付けて実行できます。
収録 LESSON: LESSON 40, LESSON 41, LESSON 42
"""

# --- 共通の準備(序章のフォント設定セル相当) ---
# Colab では 1 回だけ実行すれば OK。日本語ラベルの豆腐(□)化を防ぐ。
!pip install -q matplotlib-fontja
import matplotlib_fontja  # noqa: F401
import numpy as np
import matplotlib.pyplot as plt


# ===== LESSON 40 正方形でない行列を分ける =====

A = np.array([[3.0, 1.0], [1.0, 3.0], [2.0, 2.0]])
print(A.shape)
try:
    np.linalg.eig(A)
except np.linalg.LinAlgError as e:
    print(f"LinAlgError: {e}")

U, s, Vh = np.linalg.svd(A)
print(U.shape, s.shape, Vh.shape)
print(np.round(s, 6))

U2, s2, Vh2 = np.linalg.svd(A, full_matrices=False)
print(U2.shape, s2.shape, Vh2.shape)
print(np.allclose(U2 @ np.diag(s2) @ Vh2, A))

print(np.all(np.diff(s) <= 0))

koyu = np.linalg.eigvalsh(A.T @ A)
print(np.round(np.sqrt(koyu[::-1]), 6))
print(np.allclose(np.sqrt(koyu[::-1]), s))

C = np.array([[1.0, 2.0], [2.0, 4.0]])
print(np.round(np.linalg.svd(C)[1], 6))
print(np.linalg.matrix_rank(C))

# ===== LESSON 41 画像を小さくする =====

import matplotlib.cbook as cbook
with cbook.get_sample_data("grace_hopper.jpg") as f:
    im = plt.imread(f)
gazou = im.mean(axis=2)
print(im.shape)
print(gazou.shape)
print(f"{gazou.min():.1f}  {gazou.max():.1f}")

Ug, sg, Vhg = np.linalg.svd(gazou, full_matrices=False)
print(len(sg))
print(np.round(sg[:5], 1))

zen = (sg**2).sum()
for k in [5, 10, 50]:
    nokori = (sg[:k]**2).sum() / zen * 100
    moto = gazou.size
    ato = k * (gazou.shape[0] + gazou.shape[1] + 1)
    print(f"k={k:3d}  情報 {nokori:5.2f}%  データ {moto} → {ato} "
          f"({moto / ato:.1f}分の1)")

for k in [1, 100]:
    nokori = (sg[:k]**2).sum() / zen * 100
    print(f"k={k:3d}  情報 {nokori:5.2f}%")

# ===== LESSON 42 計算機は小数を正確に持てない =====

print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(np.isclose(0.1 + 0.2, 0.3))

print(f"{np.finfo(float).eps:.6e}")
print(f"{0.1:.20f}")

D = np.array([[0.1, 0.2], [0.3, 0.6]])
print(f"{np.linalg.det(D):.6e}")
print(np.linalg.det(D) == 0)
print(np.isclose(np.linalg.det(D), 0))

print(0.5 + 0.25 == 0.75)
print(f"{0.5:.20f}")

