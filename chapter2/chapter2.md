# 2章 Pythonの成分
## 2.1 変数、名前、オブジェクト
- ミュータブル：型の変数に入っているデータの値が変更できる。
- イミュータブル：型の変数に入っているデータの値が変更できない。
---
## 2.2 数値
- 算数演算子(+,-,*は割愛)

    演算子|意味|例|結果
    ---|---|---|--:
    /|不動小数点の除算|7 / 2|3.5
    //|整数の除算(切り捨て)|7 // 2|3
    %|剰余|7 % 3|1
    **|指数|2 ** 3|8
### 2.2.1 整数
- 連続計算はOK
```python
>>> 4 + 3 + 2 - 1
8
```
- 除数は0がNG
```python
>>> 5 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 7 // 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
>>> 8 % 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
```
- Javaと同じ、変数を計算した後に再代入する場合
```python
>>> a = 3
>>> a -= 1
>>> a
2
```
- 商と剰余を同時に取得する場合、divmod()を使う
```python
>>> divmod(9, 4)
(2, 1)
```
### 2.2.3 基数
- 2(0b/0B), 8(0o/0O), 16進数(0x/0X)
```python
>>> 0b10
2
>>> 0o10
8
>>> 0x10
16
```
### 2.2.4 型の変換
- 整数以外のデータを整数へ変換する関数：int()  
※ 小数点や指数部分を含む文字列は処理できない  
※ 精度の大きい型と小さい型を計算すると、結果は精度の大きい型の方に揃える。
### 2.2.5 intはどれぐらい大きいのか
- python2: -2147483648~2147483647(32bit, longは64bit)
- python3: 無限
### 2.2.6 浮動小数点数
- 利用サンプル：
```python
>>> print(float(True))
1.0
>>> print(float(False))
0.0
>>> print(float(98))
98.0
>>> print(float('99.9') // 10)
9.0
>>> print(float('99.9') % 10)
9.900000000000006
```
### 2.2.7 数学関数
[math --- 数学関数](https://docs.python.org/ja/3/library/math.html)
---

## 2.3 文字列
### 2.3.1 クォートを使った作成
- ダブルクォートで文字列を作るときには、文字列内にシングルクォートを入れることができる。シングルクォートで文字列を作る時には、文字列内にダブルクォートを入れることができる。
- トリプルクォートは複数行文字列を作るために使われる。行の先頭の改行、タブ、スペースは残される
```python
>>> str1 = '''There was a Young Lady of Norwar,
... \tWho casually sat in a doorway; '''
>>> print(str1)
There was a Young Lady of Norwar,
        Who casually sat in a doorway;
```
- print()は対話型インタープリタが行う自動エコーの出力は違う
print()は文字列からクォートを取り除き、文字列の内容を表示する。
さらに、表示する項目の間にスペースを追加し、末尾に改行を追加する。
```python
>>> str1
'There was a Young Lady of Norwar,\n\tWho casually sat in a doorway; '
```
### 2.3.2 str()を使った型変換
- 利用サンプル：
```python
>>> print(str(98.6))
98.6
>>> print(str(10.1e4))
101000.0
>>> print(str(True))
True
```
### 2.3.3 \によるエスケープ
- 利用サンプル：
```python
>>> print('a\tbc')
a       bc
>>> print('\'\\aaa\"')
'\aaa"
```
### 2.3.4 +による連結
- 利用サンプル：
```python
>>> print("abc" + 'def')
abcdef
>>> str2 = "abc"
>>> str2 += "def"
>>> print(str2)
abcdef
```
- 文字列と非文字列の内容と連結する場合、非文字列の内容を先にstr()で文字列に変換する必要がある
```python
>>> 'aaa' + 12345
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> 'aaa' + str(12345)
'aaa12345'
```
### 2.3.5 *による繰り返し
- 利用サンプル：
```python
>>> start = 'Na' * 4 + '\n'
>>> middle = 'Hey' * 3
>>> print(start + middle)
NaNaNaNa
HeyHeyHey
```
### 2.3.6 []による文字の抽出
- indexは0から、マイナスになると、末尾から数える(-1から)
- 文字列の長さ以上（長さ-1）のオフセットを指定すると、例外が起きる
```python
>>> letters = 'abcdefghijklmnopqrstuvwxyz'
>>> print(letters[0])
a
>>> print(letters[25])
z
>>> print(letters[-1])
z
>>> print(letters[-2])
y
```
### 2.3.7 [start:end:step]によるスライス
- [:]は、先頭から末尾までのシーケンス全体を抽出する
- [start:]は、startオフセットから末尾までのシーケンスを抽出する
- [:end]は、先頭から<font color="red">___end-1___</font>オフセットまでのシーケンスを抽出する→末尾の指定は実際のオフセットよりも一つ先でなければならない
- [start:end]は、startオフセットからend-1オフセットまでのシーケンスを抽出する
- [start:end:step]は、startオフセットからend-1オフセットまでのシーケンスを抽出した文字列に対して、step文字ごとに再抽出する

- 【トライアル】letters変数にa~zを設定し、いろいろ試す：  
    
    - sample1: letters[12:15]
    ```python
    >>> letters[12:15]
    'mno'
    ```
    オフセット|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25
    ---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
    設定値|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z
    start~end|||||||||||||12||15-1|||||||||||
    
    - sample2: letters[-3:]
    ```python
    >>> letters[-3:] 
    'xyz'
    ```
    オフセット|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25
    ---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
    設定値|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z
    start~end||||||||||||||||||||||||-3||
    
    - sample3: letters[18:-3]
    ```python
    >>> letters[18:-3] 
    'stuvw'
    ```
    オフセット|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25
    ---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
    設定値|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z
    start~end|||||||||||||||||||18||||-3-1|||
    
    - sample4: letters[-6:-2]
    ```python
    >>> letters[-6:-2] 
    'uvwx'
    ```
    オフセット|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25
    ---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
    設定値|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z
    start~end|||||||||||||||||||||-6|||-2-1||
    
    - sample5: letters[::7]
    ```python
    >>> letters[::7] 
    'ahov'
    ```
    オフセット|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25
    ---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
    設定値|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z
    start~end|0|||||||||||||||||||||||||26-1
    step|●|||||||●|||||||●|||||||●||||
    
    - sample6: letters[4:20:3]
    ```python
    >>> letters[4:20:3]
    'ehknqt'
    ```
    オフセット|0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25
    ---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
    設定値|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z
    start~end|||||4|||||||||||||||20-1||||||
    step|||||●|||●|||●|||●|||●|||●||||||
    
    - sample7: letters[-1::-1] or letters[::-1]  
    ※ステップサイズを負数を指定すると、逆にステップしていく
    ```python
    >>> letters[::-1]
    'zyxwvutsrqponmlkjihgfedcba'
    ```
### 2.3.8 len()による長さの取得
- 文字列の長さ(スペースと改行も含まれる)を取得する
    - 構文：len(対象文字列)
    - 全角文字も一文字として集計される
    - len()は文字列専用の関数ではない→文字列.len()ではない
```python
>>> len(letters)
26
>>> len('あいうえお') 
5
```

### 2.3.9 split()による分割
- 文字列を指定するセパレータで、**リスト**に分割する
    - 構文：対象文字列.split(セパレータの文字**列**)
    - セパレータを指定しない場合、セパレータとして空白文字（改行、スペース、タブ）のシーケンスを使う
```python
>>> split_t1 = 'abcd, efg hijk\nlmn\topq'
>>> print(split_t1.split())
['abcd,', 'efg', 'hijk', 'lmn', 'opq']
>>> print(split_t1.split(','))  
['abcd', ' efg hijk\nlmn\topq']
>>> print(split_t1.split('bc')) 
['a', 'd, efg hijk\nlmn\topq']
```
### 2.3.10 join()による結合
- リストを指定する結合用文字列で、文字列に結合する
    - 構文：結合用文字列.join(リスト)
```python
>>> crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
>>> crypto_string = ', '.join(crypto_list)
>>> print(crypto_string)
Yeti, Bigfoot, Loch Ness Monster
>>> crypto_string = '\n'.join(crypto_list) 
>>> print(crypto_string)
Yeti
Bigfoot
Loch Ness Monster
```

### 2.3.11 多彩な文字列操作
- 検証対象文字列.startwith(検証文字列)  
検証対象文字列の先頭は検証文字列になるか、True or Falseで返す
- 検証対象文字列.endwith(検証文字列)  
検証対象文字列の末尾は検証文字列になるか、True or Falseで返す
- 検索対象文字列.find(検索文字列)：
検索対象文字列から検索文字列が**最初**に現れる箇所のオフセットを返す<br>
見つからない場合、-1で返す。
- 検索対象文字列.rfind(検索文字列)  
検索対象文字列から検索文字列が**最後**に現れる箇所のオフセットを返す
- 検索対象文字列.count(検索文字列)  
検索対象文字列から検索文字列が何回現れたかを検索する
- 検索対象文字列.isalnum()  
検索対象文字列に含まれる文字は全て英字か数字になっているか、True or Falseで返す
```python
>>> poem = '''All that doth flow we cannot liquid name
... Or else would fire and water be the same;
... But that is liquid which is moist and wet
... Fire that property can never get.
... Then 'tis not cold that doth the fire put out
... But 'tis the wet that makes it die not doubt.'''
>>> print(poem.startswith('All'))
True
>>> print(poem.endswith('But \'tis the wet that makes it die not doubt.'))
True
>>> word = 'the'
>>> print(poem.find(word))
73
>>> print(poem.rfind(word))
214
>>> print(poem.count(word))
3
>>> poem.isalnum()
False
```

### 2.3.12 大文字と小文字の区別、配置
（操作対象文字列自体が変わらなくて、変換結果を新しい文字列として返す）
- 修正対象文字列.strip(削除対象特定文字)  
    - 修正対象文字列の両端から削除対象特定文字(指定しない場合、空白文字列として指定される)を取り除く
    - lstrip/rstripもある
    - <font color="red">要注意: 削除対象箇所に削除対象特定文字(マッチする文字列ではなく)が含まれると全てが削除される(最後の例)</font>
    ```python
    >>> setup = "\nabcdedg abcde "
    >>> setup.strip()
    'abcdedg abcde'
    >>> setup.strip("de ") 
    '\nabcdedg abc'
    >>> setup = "abcd..."
    >>> setup.strip(".") 
    'abcd'
    ```
- 修正対象文字列.capitalize()  
先頭の単語をタイトルケース
    ```python
    >>> setup = 'a duck GOES into a bar ...'
    >>> print(setup.capitalize())
    A duck goes into a bar ...
    ```
- 修正対象文字列.title()  
すべての単語をタイトルケースにする
    ```python
    >>> print(setup.title())
    A Duck Goes Into A Bar ...
    ```
- 修正対象文字列.swapcase()  
大文字小文字を逆にする
    ```python
    >>> print(setup.title().swapcase())
    a dUCK gOES iNTO a bAR ...
    ```
- 修正対象文字列.upper()  
すべての文字を大文字にする
    ```python
    >>> print(setup.upper())
    A DUCK GOES INTO A BAR ...
    ```
- 修正対象文字列.lower()  
すべての文字を大文字にする
    ```python
    >>> print(setup.upper().lower())
    a duck goes into a bar ...
    ```
- 修正対象文字列.center(スペース数)  
指定した数分のスペースの中央に修正対象文字列を配置する
    ```python
    >>> setup.center(100) 
    '                                     a duck GOES into a bar ...                                     '
    ```
- 修正対象文字列.ljust(スペース数)
- 修正対象文字列.rjust(スペース数)  
修正対象文字列をスペースで左、または右に補足する。スペース数≦文字列数の場合、スペースが補足されない
    ```python
    >>> setup.ljust(100)  
    'a duck GOES into a bar ...                                                                          '
    >>> setup.rjust(100) 
    '                                                                          a duck GOES into a bar ...'
    ```

### 2.3.13 replace()による置換
- 置換対象文字列.replace(置換元文字列, 置換後文字列, [置換回数])
最後の置換回数を省略すると、置換は全ての場所で行われる
```python
>>> setup
'a duck GOES into a bar ...'
>>> setup.replace('a', 'A', 1) 
'A duck GOES into a bar ...'
>>> setup.replace('a', 'A')    
'A duck GOES into A bAr ...'
```

### 2.3.14 その他の文字列操作関数
[文字列メソッド](https://docs.python.org/ja/3/library/stdtypes.html#string-methods)