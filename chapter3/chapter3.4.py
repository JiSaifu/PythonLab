# 3.4 辞書
# 辞書の特徴：
# 1. 要素の順序が管理されていない、代わりに個々の値に一意なキーを与える。
# 2. イミュータブル型
# 3. dictと呼ぶこともある

# 3.4.1 {}による作成f
print('--- 3.4.1 ---')
empty_dict = {}
print(empty_dict)

# Pythonでは、リスト、タプル、辞書の最後の要素の後ろにカンマを残しておいてよい。
bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top one's voice",
    "misfortune": "The kind of fortune that never misses",
}
print(bierce)

# 3.4.2 dict()を使った変換
print('--- 3.4.2 ---')
# 2要素リストのリストを辞書に変換：
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))

# 2要素のタプルのリストを辞書に変換
lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print(dict(lot))

# 2要素のリストのタプルを辞書に変換
tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print(dict(tol))

# 2字の文字列（3文字の場合はエラーになる）のリスト
los = ['ab', 'cd', 'ef']
print(dict(los))

# 2字の文字列（3文字の場合はエラーになる）のタプル
tos = ('ab', 'cd', 'ef')
print(dict(tos))

# 3.4.3 [key]による要素の追加、変更
print('--- 3.4.3 ---')
pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric'
}
print(pythons)
pythons['Gilliam'] = 'Gerry'
print(pythons)
pythons['Gilliam'] = 'Terry'
print(pythons)

# 3.4.4 update()による辞書の結合
print('--- 3.4.4 ---')
first = {'a': 1, 'b': 2}
# second辞書の同キーアイテムはfirst辞書へ更新する
second = {'b': 'platypus', 'c': 3}
first.update(second)
print(first)

# 3.4.5 delによる指定したキーを持つ要素の削除
print('--- 3.4.5 ---')
print(pythons)
del pythons['Gilliam']
print(pythons)

