# Pythonで学び直す線形代数 サンプルコード

書籍『**Pythonで学び直す線形代数**』(定義の前に、まず動かす。行列と固有値の意味)の、各章のサンプルコードです。

## 使い方

下の各章の「**Colabで開く**」ボタンを押すと、その章のコードが Google Colab で開きます。インストールは要りません。ブラウザだけで動きます。

1. ボタンを押して Colab を開く
2. 最初の「設定セル」を1回だけ ▶ で実行する
3. あとは各 LESSON のコードを上から順に ▶ で試す

本を読みながら、同じコードを自分の手で動かすのが、いちばんの近道です。数字を書きかえて ▶ を押せば、結果がどう変わるかも確かめられます。

## 章ごとのサンプルコード

本の章番号と、ここのファイル名はそろえてあります(本の第9章 → `notebooks/chapter09.ipynb`)。探している LESSON がどの章にあるかは、下の一覧から辿れます。

### 第1章 矢印を数で書く

[![Colabで開く](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/forest6511/python-linalg-relearn-samples/blob/main/notebooks/chapter01.ipynb)

- **LESSON 01** 矢印を、2つの数で書く
- **LESSON 02** 矢印を足す、伸ばす、逆向きにする
- **LESSON 03** 矢印の長さを測る
- **LESSON 04** 2本の矢印を混ぜると、どこまで届くか

→ [notebooks/chapter01.ipynb](notebooks/chapter01.ipynb)

### 第2章 行列は変形の機械

[![Colabで開く](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/forest6511/python-linalg-relearn-samples/blob/main/notebooks/chapter02.ipynb)

- **LESSON 05** 平面ぜんたいを、一度に動かす
- **LESSON 06** 行き先を2本だけ書き留める
- **LESSON 07** 掛け算を、自分の手で書く
- **LESSON 08** 4つの変形を見分ける

→ [notebooks/chapter02.ipynb](notebooks/chapter02.ipynb)

### 第3章 変形を続けてやる（行列の積）

[![Colabで開く](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/forest6511/python-linalg-relearn-samples/blob/main/notebooks/chapter03.ipynb)

- **LESSON 09** 変形を2回続けると、どうなるか
- **LESSON 10** 積の規則を、自分で導く
- **LESSON 11** 順番を変えると、答えが変わる
- **LESSON 12** 3回以上続ける、形を合わせる

→ [notebooks/chapter03.ipynb](notebooks/chapter03.ipynb)

### 第4章 連立方程式を解く

[![Colabで開く](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/forest6511/python-linalg-relearn-samples/blob/main/notebooks/chapter04.ipynb)

- **LESSON 13** 連立方程式を、行列で書き直す
- **LESSON 14** 解き方を、自分の手で書く
- **LESSON 15** 解けないときが、ある
- **LESSON 16** 行を入れ替える理由

→ [notebooks/chapter04.ipynb](notebooks/chapter04.ipynb)

### 第5章 元に戻せる変形、戻せない変形（逆行列）

[![Colabで開く](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/forest6511/python-linalg-relearn-samples/blob/main/notebooks/chapter05.ipynb)

- **LESSON 17** 元に戻す変形を探す
- **LESSON 18** 戻せない変形がある
- **LESSON 19** 逆行列で連立方程式を解かない
- **LESSON 20** 転置と逆行列を取り違えない

→ [notebooks/chapter05.ipynb](notebooks/chapter05.ipynb)

### 第6章 つぶれたかを数で判定する（行列式）

[![Colabで開く](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/forest6511/python-linalg-relearn-samples/blob/main/notebooks/chapter06.ipynb)

- **LESSON 21** つぶれたかを数だけで判定する
- **LESSON 22** 面積が負になる
- **LESSON 23** 3行3列の行列式を作る
- **LESSON 24** 教科書の方法では計算できない

→ [notebooks/chapter06.ipynb](notebooks/chapter06.ipynb)

### 第7章 無駄のない組（一次独立・基底・rank）

[![Colabで開く](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/forest6511/python-linalg-relearn-samples/blob/main/notebooks/chapter07.ipynb)

- **LESSON 25** 2本で届く範囲が変わる
- **LESSON 26** 現象に名前を付ける
- **LESSON 27** ぴったりは判定できない
- **LESSON 28** ものさしを取り替える

→ [notebooks/chapter07.ipynb](notebooks/chapter07.ipynb)

### 第8章 直角と影（内積と正射影）

[![Colabで開く](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/forest6511/python-linalg-relearn-samples/blob/main/notebooks/chapter08.ipynb)

- **LESSON 29** 向きの近さを数にする
- **LESSON 30** 図が描けない次元でも直角は分かる
- **LESSON 31** 矢印の影を落とす

→ [notebooks/chapter08.ipynb](notebooks/chapter08.ipynb)

### 第9章 変わらない方向を探す（固有値・固有ベクトル）

[![Colabで開く](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/forest6511/python-linalg-relearn-samples/blob/main/notebooks/chapter09.ipynb)

- **LESSON 32** 向きが変わらない矢印を探す
- **LESSON 33** 固有ベクトルは何の役に立つのか
- **LESSON 34** 固有値を計算で求める
- **LESSON 35** 大きい行列ではどうするか

→ [notebooks/chapter09.ipynb](notebooks/chapter09.ipynb)

### 第10章 いちばん簡単な形にする（対角化）

[![Colabで開く](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/forest6511/python-linalg-relearn-samples/blob/main/notebooks/chapter10.ipynb)

- **LESSON 36** 100回かけるのは大変か
- **LESSON 37** ものさしを取り替える
- **LESSON 38** 100乗をまとめて求める
- **LESSON 39** 対角化できない行列

→ [notebooks/chapter10.ipynb](notebooks/chapter10.ipynb)

### 第11章 大きい行列と、この先へ

[![Colabで開く](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/forest6511/python-linalg-relearn-samples/blob/main/notebooks/chapter11.ipynb)

- **LESSON 40** 正方形でない行列を分ける
- **LESSON 41** 画像を小さくする
- **LESSON 42** 計算機は小数を正確に持てない

→ [notebooks/chapter11.ipynb](notebooks/chapter11.ipynb)

---

※ このコードは書籍の理解を深めるための補助教材です。本文の説明とあわせてお使いください。
