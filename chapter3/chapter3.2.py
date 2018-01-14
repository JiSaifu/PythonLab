# 3.2 リスト
# リストの特徴：
# 1. ミュータブル（変更可能）
# 2. 同じ値が複数回収納可能

# 3.2.1 リストを作成する。
print('--- 3.2.1 ---')
# 空リストの作る
empty_list = []
another_empty_list = list()

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(weekdays)
print(another_empty_list)

# 3.2.2 list()によるほかのデータ型からリストへの変換
# split関数を利用し、文字列をリストに変換する。
# 連続セパレータ文字列が連続している部分があるときに、空文字列が作られる。
print('--- 3.2.2 ---')
birthday = '1985//6/5'
print(birthday.split('/'))

# タプルをlist()関数でリストへ変換する。
a_tuple = ('a', 'b', 'c')
print(a_tuple)
print(list(a_tuple))

# 3.2.3 [offset]で要素の取り出し
# マイナスのインデックスを使えば、末尾から逆に数えて、取り出す。
# offsetの数値はリストの長さにオーバーした場合、例外が発生する。
print('--- 3.2.3 ---')
print(weekdays[0], weekdays[-1], weekdays[-2])

# 3.2.4 リストのリスト
print('--- 3.2.4 ---')
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]

print(all_birds)
print(all_birds[0])
print(all_birds[0][1])

# 3.2.5 [offset]による要素の書き換え
print('--- 3.2.5 ---')
marxes = ['Groucho', 'Chico', 'Harpo', 'Saifu']
marxes[2] = 'Wanda'
print(marxes)

# 3.2.6 オフセットの範囲を指定したスライスによるサブシーケンスの取り出し。
# スライスを使えば、リストのサブシーケンスを取り出すことができる。
print('--- 3.2.6 ---')
print(marxes[0:2])
# リストのスライスもリストだ。
print(marxes[::2])
# 末尾から左に一つおきに要素を取り出す
print(marxes[::-2])

# 3.2.7 append()による末尾への要素の追加
print('--- 3.2.7 ---')
marxes.append('Zeppo')
print(marxes)

# 3.2.8 extend()または+=を使ったリストの結合
print('--- 3.2.8 ---')
others1 = ['Gummo', 'Karl']
others2 = ['Mary', 'Tim']
marxes.extend(others1)
print(marxes)
marxes += others2
print(marxes)
# append()を使うと、othersの要素が追加されるのではなく、
# othersが1個のリスト要素として追加されてしまう。
marxes.append(others2)
print(marxes)

# 3.2.9 insert()によるオフセットを指定した要素の追加
print('--- 3.2.9 ---')
print(marxes)
marxes.insert(0, 'Kate')
# 末尾を超えるオフセットを指定すると、append()と同じようにリストの末尾に挿入される。
marxes.insert(100, 'Mike')
# append()と同じ、リストをリストに挿入すると、1個のリスト要素として挿入される。
marxes.insert(0, others1)
print(marxes)

# 3.2.10 delによる指定したオフセットの要素を削除
print('--- 3.2.10 ---')
print(marxes)
del marxes[-2]
print(marxes)

# 3.2.11 remove()による値に基づく要素の削除
print('--- 3.2.11 ---')
print(marxes)
marxes.remove('Mike')
print(marxes)

# 3.2.12 pop()でオフセットを指定して要素を取り出し、削除する方法
print('--- 3.2.12 ---')
print(marxes)
print(marxes.pop()) #pop()とpop(-1)の実施結果は一緒。
print(marxes)
print(marxes.pop(1))
print(marxes)

# 3.2.13 index()により要素の値から要素のオフセットを知る方法
print('--- 3.2.13 ---')
print(marxes)
print(marxes.index('Saifu'))

# 3.2.14 inを使った値の有無のテスト
print('--- 3.2.14 ---')
print(marxes)
print(['Gummo', 'Karl'] in marxes, 'Saifu' in marxes, 'Ji' in marxes)
# リスト内の値があるかどうかを頻繁にチェックし、値の順序は気にせず、
# 値の重複がないのであれば、そのような値の格納、照合にはPythonの集合を使ったほうがいい。

# 3.2.15 count()を使った値の個数の計算
print('--- 3.2.15 ---')
marxes.append('Chico')
print(marxes)
print(marxes.count('Chico'))

# 3.2.16 join()による文字列への変換
print('--- 3.2.16 ---')
# リストに他の種類のデータタイプがあれば、join()はできない。
del marxes[0]
print('..'.join(marxes))

# 3.2.17 sort()による要素の並べ替え
# ・リスト関数sort()は、その場でリスト自体をソートする。
# ・汎用関数のsorted()は、ソートされたリストのコピーを返す。
print('--- 3.2.17 ---')
print(marxes)
sorted_marxes = sorted(marxes)
print(sorted_marxes)
print(marxes)
marxes.sort()
print(marxes)

number = [2, 1, 4.2, 3]
number.sort()
print(number)

# reverse=Tureを追加すると、降順になる。
number.sort(reverse=True)
print(number)

# 3.2.18 len()による長さの取得
print('--- 3.2.18 ---')
print(len(marxes))

# 3.2.19 =による代入とcopy()によるコピー
print('--- 3.2.19 ---')
a = [1, 2, 3]
# aとbは同じリストオブジェクトを参照するので、
# どちらを変更しても、両方とも反映される
b = a
a[0] = 'surprise'
print(a, b)
# 次のいずれかの方法を使えば、
# リストの値を独立の新しいリストにコピーすることができる。
c = a.copy()
d = list(a)
e = a[:]
b[1] = 'surprise too'
print(a, b, c, d, e)