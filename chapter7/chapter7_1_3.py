# 7.1 文字列
# 7.1.3 正規表現とのマッチング

# 正規表現機能は、標準モジュールのreが提供するものである
import re
# Pythonのstringモジュールは、テストのために使える文字列定数をあらかじめ定義している（以下の実験で使用する）
import string

# 7.1.3.1 match()による正確なマッチ
print('--- 7.1.3.1 ---')
# match(pattern, source)：sourceの※先頭はpatternになっているかをチェックする
source = 'Young Frankenstein'
m = re.match('You', source)
if m:
    print(m.group())

m = re.match('^You', source)
if m:
    print(m.group())

m = re.match('Frank', source)
if m:
    print(m.group())

# 7.1.3.2 search()による最初のマッチ
# search(pattern, source)：source（任意位置）にpatternが存在するかをチェックする
print('--- 7.1.3.2 ---')
m = re.search('Frank', source)
if m:
    print(m.group())

# 7.1.3.3 findall()による全てのマッチの検索。
# findall(pattern, source)：※重なり合わない全てのマッチのリストを返す（ある場合）。
# マッチ件数を求めるときによく使われる。
print('--- 7.1.3.3 ---')
m = re.findall('.n.?', source)
if m:
    print(m)

# 7.1.3.4 split()によるマッチを利用した分割。
# split(pattern, source)：パターンで文字列を分割する。
print('--- 7.1.3.4 ---')
m = re.split('n', source)
print(m)
# パターンは最後尾に存在する場合、空の文字列は最後に分割される。

# 7.1.3.5 sub()によるマッチした部分を置換
# sub(pattern, rep, source)：sourceのうち、patternにマッチするすべての部分をrepに置き換える。
print('--- 7.1.3.5 ---')
m = re.sub('n', '?', source)
print(m)
# パターンは最後尾に存在する場合、空の文字列は最後に分割される。

# 7.1.3.6 パターンの特殊文字
# string.printable:大小文字の英字と数字、空白文字と記号類を含む100種類ASCII文字
print('--- 7.1.3.6 ---')
printable = string.printable
print(printable)
print('空白文字：', re.findall('\s', printable))
print('空白文字以外：', re.findall('\S', printable))
print('英数字：', re.findall('\w', printable))
print('英数字以外：', re.findall('\W', printable))
print('数字：', re.findall('\d', printable))
print('数字以外', re.findall('\D', printable))

'''
正規表現はASCIIだけに制限されているわけではない。
\d,\wはUnicodeが数字、英数字と呼んでいるあらゆるものにマッチする。
'''
x = 'abc０１２３４' + '-/*' + '\u00ea' + '\u0115'
print(x)
print(re.findall('\d', x))
print(re.findall('\w', x))

# 7.1.3.7 パターン：メタ文字
#
print('--- 7.1.3.7 ---')
source = '''I wish I may, I wish I might
have a dish of fish tonight...'''
print('wish:', re.findall('wish', source))
print('wish or fish:', re.findall('wish|fish', source))
print('先頭の\'wish\':', re.findall('^wish', source))
print('先頭の\'I wish\':', re.findall('^I wish', source))
print('末尾の\'fish\':', re.findall('fish$', source))
print('末尾の\'fish tonight...\':', re.findall('fish tonight\.\.\.$', source))
print('wish or fish Ⅱ:', re.findall('[wf]ish', source))
print('w,s,hどれか一個以上続いているところ:', re.findall('[wsh]+', source))
print('gthの後ろに英数字以外のものが続いているところ:', re.findall('ght\W', source))
print('I（Iとスペース）の後ろにwishが続くところ:', re.findall('I (?=wish)', source))
print('wishの前にI（Iとスペース）があるところ:', re.findall('(?<=I )wish', source))
print('文字列エスケープと正規表現エスケープ共存する場合:', re.findall('\bfish', source))
print('文字列エスケープを避けたら...:', re.findall(r'\bfish', source))

# 7.1.3.8 パターン：マッチした文字列の出力の指定
#
print('--- 7.1.3.8 ---')
# パターンを括弧で囲むと、マッチは独自のグループに保存される。
m = re.search(r'(. dish\b).*(\bfish)', source)
print(m)
print(m.group())
# groups()を呼出せば、グループのタプルが得られる。
print(m.groups())

# (?P<name> expr)との形式を使うと、exprにマッチした部分はnameという名前のグループに保存される
m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
print(m)
print(m.group())
# groups()を呼出せば、グループのタプルが得られる。
print(m.groups())
print(m.group('DISH'))
print(m.group('FISH'))



