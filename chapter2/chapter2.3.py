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
# 最後の3文字を取り出す
print(letters[-3:])

print(letters[18:-3])
# 末尾6文字手前から末尾3文字手前まで
print(letters[-6:-2])
print(letters[::7])
print(letters[4:20:3])
print(letters[19::4])
print(letters[:21:5])

print(letters[-1::-1])
print(letters[::-1])
print(letters[-50::])
print('[-50:-51]:' + letters[-50:-51:])

# 2.3.8 len()による長さの取得
# len()は文字列専用の関数ではない
print('--- 2.3.8 ---')
print(len(letters))
# 全角文字も一文字とする
print(len('あいうえお'))
print(len(''))
# 下記の処理で例外が起こされる
# print(len(None))

# 2.3.9 split()による分割
print('--- 2.3.9 ---')
split_t1 = 'abcd, efg hijk\nlmn\topq'
# セパレータを指定していないsplit()は、
# セパレータとして空白文字（改行、スペース、タブ）のシーケンスを使う
print(split_t1.split())
print(split_t1.split(', '))

# 2.3.10 join()による結合
print('--- 2.3.10 ---')
crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print(crypto_string)

# 2.3.11 多彩な文字列操作
print('--- 2.3.11 ---')
poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die not doubt.'''
print(poem.startswith('All'))
print(poem.endswith('But \'tis the wet that makes it die not doubt.'))
word = 'the'
# find():最初に現れる箇所のオフセットを返す
print(poem.find(word))
print(poem.rfind(word))
print(poem.count(word))

# 2.3.12 大文字と小文字の区別、配置
print('--- 2.3.12 ---')
setup = 'a duck GOES into a bar ...'
print(setup)
# strip():両端から'r', ' ', '.'のシーケンスを取り除こう
# 文字列はイミュータブルなので、setup文字列を実際に書き換えない
print(setup.strip('r .'))
# 先頭の単語を大文字にし、ほかを小文字にする
print(setup.capitalize())
# 全ての単語をタイトルケースにする
print(setup.title())
# 全ての文字を大文字にする
print(setup.upper())
# 全ての文字を小文字にする
print(setup.lower())
# 大文字小文字を逆にする
print(setup.swapcase())
# 指定したスペースの中で文字列をどのように配置するかを決める
print(setup.center(30))
print(setup.ljust(30))
print(setup.rjust(30))
# 2.3.13 replace()による置換
replace_t1 = 'aaaaaaacccccccc'
print(replace_t1.replace('a', 'b'))
# 置換関数は第三引数で指定することができる
print(replace_t1.replace('a', 'b', 3))




