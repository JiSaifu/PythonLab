# 8.1 ファイル入出力

# ファイルを開く：open(filename, mode)
"""
    mode:2文字
        最初の文字：
        ・r: 読取り専用（ファイルが存在しなければ、エラーになる）
        ・w: 書き込み、ファイルが存在しなければ、作る；存在すれば、上書きする
        ・x: 書き込み、ファイルが存在しない時だけ使える。
            既存ファイルに誤りに上書きすることを防止するためのモード
        ・a: 書き込み、ファイルが存在しなければ、作る；存在すれば、追記する
        第2字目：ファイルのタイプ
        ・t(デフォルト):テキストファイル
        ・bバイナリファイル（バイナリの内容のみ書き込める）
"""
# 8.1.1 write()によるテキストファイルへの書き込み
print('--- 8.1.1 ---')
poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''

poem2 = '''I like my daughter.'''
print(len(poem))

fout1 = open('file_dir/relativity1', 'wt')
fout2 = open('file_dir/relativity2', 'wt')
# write()関数は、書き込んだバイト数を返す。
rtnByte = fout1.write(poem + poem2)
print(rtnByte)
# print()関数を利用し、file=XXXをしても、writeと同じくファイルへ書き込める
'''
引数説明：
・sep:複数書き込む対象文字列（以下のpoem, poem2）間に追加されるセパレータ（デフォルトはスペース' '）
・end:末尾の文字列。デフォルトで改行('\n')になる
'''
print(poem, poem2, file=fout2, sep='', end='')
fout2.close()

# ファイルが大きい場合、全部書き込むまでチャンクに分けて書き込む方法：
fout3 = open('file_dir/relativity3', 'wt')
size = len(poem)
chunk = 100
offset = 0
while True:
    if offset > size:
        break
    fout3.write(poem[offset: offset + chunk])
    offset += chunk

fout3.close()

# 上書きを防止する方法、モードをxにする
fout4 = None
try:
    fout4 = open('file_dir/relativity4', 'xt')
    fout4.write(poem)
except FileExistsError as fee:
    print('relativity4 already exist! That was a close one!')
finally:
    if fout4 is not None:
        fout4.close()

# 8.1.2 read(), readline(), readlines()によるテキストファイルの読み出し
# read():引数を指定しないと、ファイル全体を一度読みだすことができる（大きなファイルに要注意）
print('--- 8.1.2 ---')
fin = open('poem', 'rt')
poem = fin.read()
len(poem)
fin.close()

# read(size):sizeを指定すれば、一度に返すデータの量を制限できる
poem = ''
fin = open('poem', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment
    print(len(poem))
fin.close()

# readline():ファイルを一行すつ読み出す
poem = ''
fin = open('poem', 'rt')
chunk = 100
while True:
    line = fin.readline()
    if not line:
        break
    poem += line
    print(len(poem))
fin.close()

# イテレータを使うと、readline()と同じくファイル内容を読み出せる、そしてコード量が少ない。
poem = ''
fin = open('poem', 'rt')
for line in fin:
    poem += line

fin.close()
len(poem)

fin = open('poem', 'rt')
lines = fin.readlines()
fin.close()

print(lines)
print(len(lines), 'line read')
for line in lines:
    # 最後の改行を''と設定するによって、文末に改行が追加されないようになる。
    print(line, end='')

# 8.1.5 withによるファイルの自動的にクローズ
print('--- 8.1.5 ---')
# Pythonは、オープンファイルなどをクリーンアップするためにコンテキストマネージャを持っている。
# 文法：with expression as variable
'''
コンテキストマネージャの下のコードブロック（この場合は1行だけ）が正常に終わるか例外生成によって終わると、
ファイルは自動的に閉じられる。
'''
with open('poem', 'wt') as fout:
    fout.write(poem)


# 8.1.6 seek()による位置の変更
print('--- 8.1.6 ---')
# 以下の関数はバイナリファイルに最も役に立つ。
# テキストファイルにはASCII以外の文字があれば、オフセットの計算は難しい（1文字は何バイトになる可能性があるから）

# バイナリファイルを作成する
with open('bin_file', 'wb') as fout:
    fout.write(bytes(range(0, 256)))

with open('bin_file', 'rb') as fin:
    # tell():現在のファイルの先頭からのオフセットをバイト単位で返す。
    print(fin.tell())
    # seek(offset):ファイル内の別のオフセットに移動し、移動後のオフセットも返してくる。offset:移動先のオフセット
    fin.seek(255)
    bdata = fin.read()
    print(len(bdata), bdata)

    '''
    seek(offset, origin)のように第2引数を指定することもできる。
    ・ originが0（デフォルト）なら、先頭からoffsetバイトの位置に移動する
    ・ originが1なら、現在の位置からoffsetバイトの位置に移動する
    ・ originが2なら、末尾からoffsetバイトの位置に移動する
    '''
    # なので、末尾のバイトへ遷移させるために、ファイル全体のバイト数を分かる必要はない。
    print(fin.seek(-1, 2))
    # ファイルの現在位置からのシーク例
    print(fin.seek(254, 0))
    print(fin.seek(1, 1))
    print(fin.read()[0])
