# 2.3 文字列

# 2.3.1 クォートを使った作成
print('--- 2.3.1 ---')
print("'Nay,' said the naysayer.")
print('A "two by four" is actually 1 1/2" X 3 1/2".')

# トリプルクォートは複数行文字列を作るために使われる
# 行の先頭の改行、タブ、スペースは残される
str1 = '''There was a Young Lady of Norwar,
\tWho casually sat in a doorway; '''
print(str1)

# print()は対話型インタープリタが行う自動エコーの出力は違う
# print()は文字列からクォートを取り除き、文字列の内容を表示する。
# さらに、表示する項目の間にスペースを追加し、末尾に改行を追加する。
print(99, 'bottle', 'would be enough.')

# 2.3.2 str()を使った型変換
print('--- 2.3.2 ---')
print(str(98.6))
print(str(10.1e4))
print(str(True))

# 2.3.3 \によるエスケープ
print('--- 2.3.3 ---')
print('a\tbc')
print('\'\\aaa\"')

# 2.3.4 +による連結
print('--- 2.3.4 ---')
print("abc" + 'def')
str2 = "abc"
str2 += "def"
print(str2)

# 2.3.5 *による繰り返し
print('--- 2.3.5 ---')
start = 'Na' * 4 + '\n'
middle = 'Hey' * 3 + '\n'
print(start + middle)

# 2.3.6 []による文字の抽出
print('--- 2.3.6 ---')
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[0])
# マイナスになると、末尾から数える(-1から)
print(letters[-1])
print(letters[-2])

# 2.3.7 [start:end:step]によるスライス
print('--- 2.3.7 ---')
# ・[:]は、先頭から末尾までのシーケンス全体を抽出する
# ・[start:]は、startオフセットから末尾までのシーケンスを抽出する
# ・[:end]は、先頭からend-1オフセットまでのシーケンスを抽出する
# ・[start:end]は、startオフセットからend-1オフセットまでのシーケンスを抽出する
# ・[start:end:step]は、step文字ごとにstartオフセットからend-1オフセットまでのシーケンスを抽出する
letters = 'abcdefghijklmnopqrstuvwxyz'
print(letters[:])
print(letters[20:])
print(letters[1:3])
print(letters[-3:])