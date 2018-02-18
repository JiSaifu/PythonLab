# 4.3 if、elif、elseによる比較
print('--- 4.3 ---')
disaster = True
if disaster:
    # print：通常画面にメッセージを表示するPythonの組み込み関数
    print("Woe!")
else:
    print("Whee")
    print("Whee")
# pythonでは、インデントによってif、else節が、
# どのように対応しているかを表現する
print("out of if block")

color = "puce"
if color == "red":
    print("It's a tomato")
elif color == "green":
    print("It's a green pepper")
elif color == "bee purple" :
    print("I don't know what it is, but only bees can see it")
else:
    print("I've never heard of the color", color)

# 1個の変数で複数の比較をandする場合、Pythonでは次のように書くことができる
# もっと長い比較を書くこともできる。
x = 7
print(5 < x < 10 < 999)

# --- 4.3.1 ---
# Falseと見なされるもの
# ブール値：False
# null：None
# 整数のゼロ：0
# floatのゼロ：0.0
# 空文字列：''
# 空リスト、タプル、辞書、集合：[], (), {}, set()
