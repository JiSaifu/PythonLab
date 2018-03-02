# 7.1 文字列
# 7.1.1 Unicode
# 7.1.1.1 Python3のUnicode文字列
# Python3の文字列はUnicode文字列、バイト列ではない。

#Pythonでは、\u、または\N{name}を使って、一つの文字の指定はできる
#\uの後ろは4個の16進数
#\N{name}のnameは標準の名前
#unicodedataモジュールには、双方向の変換関数が含まれる。

print('--- 7.1.1.1 ---')
def unicode_test(value):
    import unicodedata
    # name(value):Unicode文字で大文字の名前を検索する
    name = unicodedata.name(value)
    # lookup(name):名前（大小文字を区別しない）でUnicode文字を検索
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))


unicode_test('\u00e9')
print('caf\u00e9')
print('caf\N{LATIN SMALL LETTER E WITH ACUTE}')

# 文字列のlen関数は、バイト数ではなく、Unicodeの文字数を数える
print(len('\u00e9'))

# 7.1.1.2　UTF-8によるエンコード、デコード
# エンコード：文字列　⇒　バイト列
# デコード：バイト列　⇒　文字列

# 7.1.1.3　エンコーディング
# 文字列.encode()
# 第一引数：エンコーディング名（ascii, utf-8, latin-1[ISO 8859-1], cp-1252...）
print('--- 7.1.1.3 ---')
snowman = 'I like \u2603'
print(snowman)
ds = snowman.encode('utf-8')
print(ds)
# 'I like 'の長さはasciiと同じ7バイトで、utf-8の長所である。
print(len(ds))


# 変換できない場合、エラーになる
# ds = snowman.encode('ascii')

# 変換できない場合、エラーにならないように、encode()の第二引数を設定する
# 'ignore': 変換できないものを捨てる
print(snowman.encode('ascii', 'ignore'))
# 'replace': 変換できないものを「?」に置き換える
print(snowman.encode('ascii', 'replace'))
# 'backslashreplace': unicode-escape形式のPython Unicode文字列を生成する
print(snowman.encode('ascii', 'backslashreplace'))
# 'xmlcharrefreplace': web pageで使えるエンティティ文字列を生成する
print(snowman.encode('ascii', 'xmlcharrefreplace'))

# 7.1.1.4 ディコーディング
# 外部ソースからテキストを取り出した時、そのテキストはバイト列としてエンコードされている。
# デコードする時に、エンコードされた時に使ったencodingを知らなければならない。

place = 'caf\u00e9'
print(place)
print(type(place))

place_byte = place.encode('utf-8')
print(place_byte)
print(type(place_byte))

place2 = place_byte.decode('utf-8')
print(place2)
# エンコーディングを間違えると、違うものがdecodeされ、またはエラーになる。
place2 = place_byte.decode('windows-1252')
print(place2)
