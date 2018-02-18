# 3.3 タプル
# タプルの特徴：
# 1. イミュータブル（変更不能）
# 2. 同じ値が複数回収納可能

# 3.3.1 ()を使ったタプルの作成
print('--- 3.3.1 ---')
# 空タプルを作る
empty_tuple = ()
print(empty_tuple)

# 要素が1個のタプルも末尾にカンマを付けて作る。
one_marx = 'Groucho',
print(one_marx)

# 要素が複数ある場合には、すべての要素の後ろにカンマをつける
# （最後の要素の後ろのカンマは省略できる）
# 括弧で囲んで定義することで、タプルだとわかりやすくなる。
marx_tuple = 'Groucho', 'Chico', 'Harpo',
print(marx_tuple)

# タプルを使えば、一度に複数の変数を代入できる。
a, b, c = marx_tuple
print(a, b, c)

# タプルを使えば、一時変数を使わずに一つの分で値を交換できる。
password = 'swordfish'
icecream = 'abcdefg'
password, icecream = icecream, password
print(password, icecream)

# 変換関数のtuple()を使うとほかのものからタプルを作られる。
marx_list = ['Groucho', 'Chico', 'Harpo']
print(tuple(marx_tuple))

# 3.3.2 タプルとリストの比較
# ・タプルは、消費スペースが小さい
# ・タプルの要素は、誤って書き換える危険がない
# ・タプルは辞書のキーとして使える
# ・名前付きタプル（6.14.1参照）は、オブジェクトの単純な代用品として使える
# ・関数の引数は、タプルとして渡される（4.7参照）


