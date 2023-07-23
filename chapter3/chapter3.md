# 3章 Pythonの具：リスト、タプル、辞書、集合
## 3.1 リストとタプル
- ミュータブル(mutable)：型の変数に入っているデータの値が変更できる。
- イミュータブル(immutable)：型の変数に入っているデータの値が変更できない。
---
## 3.2 リスト
### 3.2.1 []またはlist()による作成
- 以下の通り、[]またはlist()によって空リストを作成する
```python
>>> []
[]
>>> list()
[]
>>> ['a', 'b', 'c']
['a', 'b', 'c']
>>> list('abc')    
['a', 'b', 'c']
```
### 3.2.2 list()によるほかのデータ型からリストへの変換
- 文字列をリストへ変換する
```python
>>> list('abc')    
['a', 'b', 'c']
```
- タプルをリストへ変換する
```python
>>> a_tuple = ('a', 'b', 'c')
>>> print(a_tuple)
('a', 'b', 'c')
>>> print(list(a_tuple))
['a', 'b', 'c']
```
### 3.2.3 [offset]を使った要素の取り出し
- 文字列の操作方法と同じ、[start:end:step]の形で取り出しができる
```python
>>> weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
>>> print(weekdays[0], weekdays[-1], weekdays[-2])
Monday Sunday Saturday
```
### 3.2.4 リストのリスト
- リストは型がまちまちの要素を格納でき、使える型にはほかのリストも含まれる。
```python
>>> small_birds = ['hummingbird', 'finch']
>>> extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
>>> carol_birds = [3, 'French hens', 2, 'turtledoves']
>>> all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
>>> print(all_birds)
[['hummingbird', 'finch'], ['dodo', 'passenger pigeon', 'Norwegian Blue'], 'macaw', [3, 'French hens', 2, 'turtledoves']]
>>> print(all_birds[0])
['hummingbird', 'finch']
>>> print(all_birds[0][1])
finch
```
### 3.2.5 [offset]による要素の書き換え
- リストはミュータブルのため、中身の要素を書き換えることができる
```python
>>> marxes = ['Groucho', 'Chico', 'Harpo', 'Saifu']
>>> marxes[2] = 'Wanda'
>>> marxes
['Groucho', 'Chico', 'Wanda', 'Saifu']
```
### 3.2.6 オフセットの範囲を指定したスライス(slice)によるサブシーケンスの取り出し
- 文字列と同じくスライスによって範囲を指定したリストの取得は可能  
    ※ 取得した要素が1つになっても、1つの要素になるリストになる
```python
>>> print(marxes[0:2])
['Groucho', 'Chico']
>>> print(marxes[::4]) 
['Groucho']
# Grouchoを始め要素として、取得する。そして、chicoを増分の第一要素として、4つの要素を数えて取得する。
# 4つ目の要素がないため、何も取得されない
>>> print(marxes[::-2])
['Saifu', 'Chico']
```
### 3.2.7 append()による末尾への要素の追加
- リスト.append(追加対象要素): リストの末尾に**一つずつ**要素を追加していく方法  
    ※ リストをappendする場合、1つの要素として追加される。リストとして追加してほしい場合、extend()または+=を利用する
```python
>>> marxes.append('Zeppo')
>>> print(marxes)
['Groucho', 'Chico', 'Wanda', 'Saifu', 'Zeppo']
>>> marxes.append(['Mike', 'Tom'])
>>> marxes
['Groucho', 'Chico', 'Wanda', 'Saifu', 'Zeppo', ['Mike', 'Tom']]
```
### 3.2.8 extend()または+=を使った**リスト**の結合
- リスト1.extend(リスト2): リスト1の末尾にリスト2を追加して、1つにまとめる
```python
>>> marxes.extend(['Mike', 'Tom'])
>>> marxes
['Groucho', 'Chico', 'Wanda', 'Saifu', 'Zeppo', 'Mike', 'Tom']
# marxes += ['Mike', 'Tom']も同じ結果
# 文字列をextendで実行する場合、文字列の各文字をリストに変換され、追加されてしまう
>>> marxes.extend('mama')
marxes
['Groucho', 'Chico', 'Wanda', 'Saifu', 'Zeppo', 'Mike', 'Tom', 'm', 'a', 'm', 'a']
```
### 3.2.9 insert()によるオフセットを指定した**要素**の追加
- リスト.insert(オフセット, インサート対象要素): 対象要素をリストの指定オフセット要素の**直前**に追加する
    ※ appendと同じく追加内容を1つの要素とする  
    ※ オフセットがリストの末尾に超えても例外が発生せず、要素をリストの末尾に追加する  
    ※ オフセットを-1と指定する場合、末尾に要素を追加するではなく、末尾要素の直前に追加する
```python
>>> marxes.insert(100, ['tanjiro', 'netsuko']) 
>>> marxes
['Groucho', 'Chico', 'Wanda', 'Saifu', 'Zeppo', ['Mike', 'Tom'], ['tanjiro', 'netsuko']]
>>> marxes.insert(-1, 'inosuke')              
>>> marxes
['Groucho', 'Chico', 'Wanda', 'Saifu', 'Zeppo', ['Mike', 'Tom'], 'inosuke', ['tanjiro', 'netsuko']]
```
### 3.2.10 delによる指定したオフセットの要素の削除
- del リスト[オフセット]: リストから指定したオフセットの要素を削除する  
    ※ delはPythonの文であり、リストのメソッドではない。なので、list.del()ではない
```python
>>> del marxes[-1]
>>> marxes
['Groucho', ['tanjiro', 'netsuko'], 'Chico', 'Wanda', 'Saifu', 'Zeppo', ['tanjiro', 'netsuko'], ['Mike', 'Tom'], 'inosuke']
```
### 3.2.11 remove()による値に基づく要素の削除
- リスト.remove(削除対象要素の値): リストから指定した削除対象要素の値を検索し、**一番最初にマッチする要素**を削除する
- 削除対象要素の値はリストに存在しない場合、例外になる
```python
>>> marxes
['Groucho', ['tanjiro', 'netsuko'], 'Chico', 'Wanda', 'Saifu', 'Zeppo', ['tanjiro', 'netsuko'], ['Mike', 'Tom'], 'inosuke']
>>> marxes.remove(['tanjiro', 'netsuko'])
>>> marxes
['Groucho', 'Chico', 'Wanda', 'Saifu', 'Zeppo', ['tanjiro', 'netsuko'], ['Mike', 'Tom'], 'inosuke']
>>> marxes.remove(['error'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```
### 3.2.12 pop()でオフセットを指定して要素を取り出し、削除する方法
- リスト.pop([オフセット]): リストからオフセットを指定して要素を取り出し、削除する
    ※ pop(0): 先頭要素を取り出し、削除 -> FIFO
    ※ pop() or pop(-1): 末尾要素を取り出し、削除 ->LIFO
```python
>>> print(marxes.pop())
inosuke
>>> print(marxes)
['Groucho', 'Chico', 'Wanda', 'Saifu', 'Zeppo', ['tanjiro', 'netsuko'], ['Mike', 'Tom']]
>>> print(marxes.pop(1))
Chico
>>> print(marxes)
['Groucho', 'Wanda', 'Saifu', 'Zeppo', ['tanjiro', 'netsuko'], ['Mike', 'Tom']]
```
### 3.2.13 index()により要素の値から要素のオフセットを知る方法
- リスト.index(要素の値): リストから指定した要素の値を検索し、一番最初にマッチする要素のオフセットを返す
- removeと同じく、対象要素がなければ、例外になる
```python
>>> print(marxes)
['Wanda', 'Saifu', 'Zeppo', ['tanjiro', 'netsuko'], ['Mike', 'Tom']]
>>> marxes.index('Saifu')
1
```
### 3.2.14 inを使った値の有無のテスト
- 検索対象要素の値 in リスト: 検索対象要素の値はリストに存在するか、True or Falseで返す
```python
>>> print(['tanjiro', 'netsuko'] in marxes, 'Saifu' in marxes, 'Ji' in marxes) 
True True False
```
### 3.2.15 count()を使った値の個数の計算
- リスト.count(検索対象要素の値): 特定の値がリスト内に何個含まれるか数える
    ※ count()関数は必ず1つの引数が必要で、リスト全体の要素数を数える場合、汎用関数len()を使う
```python
>>> marxes = ['Wanda', 'Saifu', 'Zeppo', ['tanjiro', 'netsuko'], ['Mike', 'Tom'], ['Mike', 'Tom']] 
>>> marxes.count(['Mike', 'Tom'])
2
```
### 3.2.16 join()による文字列への変換
- 区切り文字列.join(結合対象リスト): 区切り文字列を使って、結合対象リスト中の文字列要素を1つの文字列に結合する
    ※ joinは**文字列**のメソッドのため、リストを変換する場合、リストの中身に文字列要素しか含まれない
```python
>>> marxes = ['Chico', 'Wanda', 'Saifu']
>>> ' * '.join(marxes)
'Chico * Wanda * Saifu'
```
### 3.2.17 sort()による要素の並べ替え
- リスト.sort(): **リスト関数**のsort()を実行すると、リスト自体を昇順でソートする
- sorted(リスト)： **汎用関数**のsort**ed**()を実行すると、昇順でソートされたリストのコピーを返すが、元リストのソート順は変わらない
    ※ sort()のデフォルトソート順は昇順だが、reverse=True引数を追加すれば降順になる
```python
>>> print(marxes)
['Chico', 'Wanda', 'Saifu']
>>> sorted_marxes = sorted(marxes)
>>> print(sorted_marxes)
['Chico', 'Saifu', 'Wanda']
>>> print(marxes)
['Chico', 'Wanda', 'Saifu']
>>>
>>> marxes.sort()
>>> print(marxes)
['Chico', 'Saifu', 'Wanda']
>>>
>>> number = [2, 1, 4.2, 3]
>>> number.sort()
>>> print(number)
[1, 2, 3, 4.2]
>>>
>>> number.sort(reverse=True)
>>> print(number)
[4.2, 3, 2, 1]
```
### 3.2.18 len()による長さの取得
- len(リスト): リスト内の要素数を返す
```python
>>> len(number)
4
```
### 3.2.19 =による代入とcopy()によるコピー
- リストにおいて（普通の変数と違う）、=による代入は**アドレス**の代入になる
- 以下の方法はリスト値をコピーし、新しいリストを作成する
    - **新リスト = 元リスト.copy() <- これを使ったほうがわかりやすいかな**
    - 新リスト = list(元リスト)
    - 新リスト = 元リスト[:]
```python
>>> a = [1, 2, 3]
>>> b = a
>>> a[0] = 'surprise'
>>> a
['surprise', 2, 3]
>>> b
['surprise', 2, 3]
>>> c = a.copy()
>>> c
['surprise', 2, 3]
>>> d = list(a)
>>> e = a[:]
>>> b[1] = 'surprise too'
>>> a
['surprise', 'surprise too', 3]
>>> b
['surprise', 'surprise too', 3]
>>> c
['surprise', 2, 3]
>>> d
['surprise', 2, 3]
>>> e
['surprise', 2, 3]
```
## 3.3 タプル
リストと同様に任意の要素を集めたシーケンスだが、**イミュータブル**である(定数リストと言うべき)
### 3.3.1 ()を使ったタプルの作成
- 空タプルの作成
```python
>>> empty_tuple = ()
>>> empty_tuple       
()
```
- 初期値のあるタプルの作成: ()なしでもOKだが、あったほうがわかりやすい
```python
>>> marx_tuple = ('Groucho', 'Chico', 'Harpo')
# or marx_tuple = 'Groucho', 'Chico', 'Harpo'
>>> print(marx_tuple)
('Groucho', 'Chico', 'Harpo')
```
- 一度に複数変数を代入
```python
>>> a, b, c = marx_tuple
>>> print(a, b, c)
Groucho Chico Harpo
```
- 一時変数は不要で複数の変数値の交換
```python
>>> a, b, c = c, a, b
>>> a, b, c
('Harpo', 'Groucho', 'Chico')
```
- tuple(リストのようなほかのもの): リストのようなほかのものをタプルへ変換
```python
>>> a = tuple(['Harpo', 'Groucho', 'Chico'])
>>> a
('Harpo', 'Groucho', 'Chico')
```
### 3.3.2 タプルとリストの比較
- append(), insert()など値を変更する関数はない
- メリット
    - タプルは、消費スペースが小さい
    - タプルの要素は、誤って書き換える危険がない
    - タプルは辞書のキーとして使える
    - 名前付きタプルは、オブジェクトの単純な代用品として使える
    - 関数の引数は、タプルとして渡される

## 3.4 辞書
- ミュータブル(キー/値要素を追加、削除、変更することができる)
- キーにて値を取得する
- キーは文字列の場合が多いが、イミュータブル型ならでよい（ブール、整数、float、タプル、文字列など、混ぜてもOK）
- Pythonでは、辞書をdictと呼ぶこともある
### 3.4.1 {}による作成
- {}で空の辞書を作成する
```python
>>> empty_dict = {}
>>> empty_dict
{}
```
- {k1:v1,k2:v2...}による初期値の付与
```python
>>> bierce = {
...     "day": "A period of twenty-four hours, mostly misspent",
...     "positive": "Mistaken at the top one's voice",
...     "misfortune": "The kind of fortune that never misses",
... }
>>> print(bierce)
{'day': 'A period of twenty-four hours, mostly misspent', 'positive': "Mistaken at the top one's voice", 'misfortune': 'The kind of fortune that never misses'}
```
### 3.4.2 dict()を使った変換
- dict(二つの値のシーケンス): 二つの値のシーケンスを辞書に変換できる
    - 辞書内のキーの順序は決まっておらず、要素を追加したときの順序とは異なる場合がある
```python
>>> # 2要素リストのリストを辞書に変換：
>>> lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
>>> print(dict(lol))
{'a': 'b', 'c': 'd', 'e': 'f'}
>>>
>>> # 2要素のタプルのリストを辞書に変換（2要素のタプルのタプルもOK）
>>> lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
>>> print(dict(lot))
{'a': 'b', 'c': 'd', 'e': 'f'}
>>>
>>> # 2要素のリストのタプルを辞書に変換
>>> tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
>>> print(dict(tol))
{'a': 'b', 'c': 'd', 'e': 'f'}
>>>
>>> # 2字の文字列（3文字の場合はエラーになる）のリスト
>>> los = ['ab', 'cd', 'ef']
>>> print(dict(los))
{'a': 'b', 'c': 'd', 'e': 'f'}
>>>
>>> # 2字の文字列（3文字の場合はエラーになる）のタプル
>>> tos = ('ab', 'cd', 'ef')
>>> print(dict(tos))
{'a': 'b', 'c': 'd', 'e': 'f'}
```
### 3.4.3 [key]による要素の追加、変更
- キーは一意になる、同じキーに2回値を付与する場合、最後に付与する値が採用される
```python
>>> pythons = {     
...     'Chapman': 'Graham',
...     'Cleese': 'John',
...     'Idle': 'Eric'
... }
>>> print(pythons)
{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric'}
>>> pythons['Gilliam'] = 'Gerry'
>>> print(pythons)
{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Gilliam': 'Gerry'}
>>> pythons['Gilliam'] = 'Terry'
>>> print(pythons)
{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Gilliam': 'Terry'}
```
### 3.4.4 update()による辞書の結合
- 更新元辞書.update(更新対象辞書): 更新対象辞書の内容にて更新元辞書へ挿入/更新する
```python
>>> first = {'a': 1, 'b': 2}
>>> second = {'b': 'platypus', 'c': 3}
>>> first.update(second)
>>> print(first)
{'a': 1, 'b': 'platypus', 'c': 3}
```
### 3.4.5 delによる指定したキーを持つ要素の削除
- del 更新対象辞書[削除対象のキー]: 指定したキーの要素を辞書から削除する
```python
>>> print(pythons)
{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Gilliam': 'Terry'}
>>> del pythons['Gilliam']
>>> print(pythons)
{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric'}
```
### 3.4.6 clear()による全ての要素の削除
- クリア対象辞書.clear(): クリア対象辞書を空辞書({})にする
```python
>>> pythons = {'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric'}
>>> pythons.clear()
>>> pythons
{}
```
### 3.4.7 inを使ったキーの有無のテスト
- 検索対象のキー in 検索対象の辞書: 検索対象の辞書に検索対象のキーの要素が存在するかTrue or Falseで返す
```python
>>> pythons = {'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric'}
>>> 'Chapman' in pythons
True
>>> 'ironman' in pythons
False
```
### 3.4.8 [key]による要素の取得
- 辞書[キー]: もっとも一般的な方法で対応する値を取得できる。但し、キーが存在しなければ例外が発生する
```python
>>> pythons
{'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric'}
>>> pythons['Chapman'] 
'Graham'
>>> pythons['ironman'] 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'ironman'
```
- 辞書専用のget()関数を利用することで、キーが存在しない場合、例外の発生を回避できる
```python
>>> pythons.get('Chapman')
'Graham'
# 存在しないキーだったら、Noneを返す(対話型インタープリタには何も表示されない)
>>> pythons.get('ironman')   
>>> 
# オプションにデフォルト値を設定することでその値を返す
>>> pythons.get('ironman', 'Tony') 
'Tony'
```
### 3.4.9 keys()によるすべてのキーの取得
- 辞書.keys(): キーの一覧をイテラブルなキーのビューであるdict_keys()の形で返す(必要な時間とメモリを使わない)。リストで返す必要な場合、list()で変換する
```python
>>> pythons.keys()
dict_keys(['Chapman', 'Cleese', 'Idle'])
>>> list(pythons.keys())
['Chapman', 'Cleese', 'Idle']
```
### 3.4.10 values()によるすべての値の取得
- 辞書.values(): 値の一覧をイテラブルなキーのビューであるdict_values()の形で返す(必要な時間とメモリを使わない)。リストで返す必要な場合、list()で変換する
```python
>>> pythons.values()     
dict_values(['Graham', 'John', 'Eric'])
>>> list(pythons.values()) 
['Graham', 'John', 'Eric']
```
### 3.4.11 items()によるすべてのキー/値ペアの取得
- 辞書.items(): キー/値ペアの一覧をインタブルなキーのビューであるdict_items()の形で返す(必要な時間とメモリを使わない)。リストで返す必要な場合、list()で変換する
    ※ キー/値ペアはタプルの形で返される
```python
>>> pythons.items()
dict_items([('Chapman', 'Graham'), ('Cleese', 'John'), ('Idle', 'Eric')])
>>> list(pythons.items())
[('Chapman', 'Graham'), ('Cleese', 'John'), ('Idle', 'Eric')]
```
### 3.4.12 =による代入とcopy()によるコピー
- リストの場合と同様に、辞書に変更を加えると、その辞書を参照しているすべての名前に影響が及ぶ
- 別の辞書に実際にキー/値ペアをコピーしたい場合は、copy()を使えばよい

## 3.5 集合
### 3.5.1 set()による作成
- set() or {}(1つ以上の要素が必要、そうでなければ辞書になる)にて集合を作成する
- 辞書と同じく、集合の要素には順序がない
```python
>>> empty_set = set()
>>> empty_set
set()
>>> even_number = {0, 2, 4, 6, 8}
>>> even_number
{0, 2, 4, 6, 8}
```
### 3.5.2 set()によるほかのデータ型から集合への変換
- リスト、文字列、タプル、辞書から重複する値を取り除けば集合を作ることができる
```python
>>> set('letter')
{'r', 'e', 't', 'l'}
>>> set(['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'])
{'Mason-Dixon', 'Prancer', 'Dancer', 'Dasher'}
>>> set(('Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'))
{'Mason-Dixon', 'Prancer', 'Dancer', 'Dasher'}
# 辞書をset()に渡すと、キーだけが使われる
>>> set({'apple': 'red', 'orange': 'orange', 'cherry': 'red'})
{'apple', 'orange', 'cherry'}
```
### 3.5.3 inを使った値の有無をテスト
- 検索対象 in 集合: 検索対象が集合に存在するか、True or Falseを返す
```python
>>> 'apple' in {'apple', 'orange', 'cherry'}
True
>>> 'banana' in {'apple', 'orange', 'cherry'} 
False
```
### 3.5.4 組み合わせと演算
- 積集合: 
    - 集合a & 集合b
    - 集合a.intersection(集合b)
    ```python
    >>> a = {1, 2, 3}
    >>> b = {2, 3, 4}
    >>> a & b
    {2, 3}
    >>> a.intersection(b)
    {2, 3}
    ```
- 和集合:
    - 集合a | 集合b
    - 集合a.union(集合b)
    ```python
    >>> a | b
    {1, 2, 3, 4}
    >>> a.union(b)
    {1, 2, 3, 4}
    ```
- 差集合(第1の集合には**含まれているものの**、第2の集合に含まれないもの):
    - 集合a - 集合b
    - 集合a.difference(集合b)
    ```python
    >>> a - b
    {1}
    >>> a.difference(b)
    {1}
    >>> b - a
    {4}
    ```
- 排他的OR(どちらか片方に含まれているが、両方には含まれていない要素の集合):
    - 集合a ^ 集合b
    - 集合a.symmetric_difference(集合b)
    ```python
    >>> a ^ b
    {1, 4}
    >>> a.symmetric_difference(b)
    {1, 4}
    ```
- 部分集合(片方の集合がもう片方の集合ぶ一部になっているか)
    - 集合a <= 集合b
    - 集合a.issubset(集合b)
    - どの集合でも、自分自身の部分集合になっている
    ```python
    >>> a = {2, 3}
    >>> b = {1, 2, 4, 3}
    >>> a <= b
    True
    >>> a.issubset(b)
    True
    >>> b <= a
    False
    ```
- 真部分集合(第2の集合は第1の集合のすべての要素に加えて**別の要素を持っていなければならない**)
    - 集合a < 集合b
    ```python
    >>> a < b
    True
    ```
- 上位集合(部分集合の逆)
    - 集合a >= 集合b
    - 集合a.issuperset(集合b)
    ```python
    >>> b >= a
    True
    >>> b.issuperset(a)
    True
    ```
- 真上位集合(真部分集合の逆)
    - 集合a > 集合b
    ```python
    >>> b > a
    True
    ```

## 3.6 データ構造の比較
- リスト: []
- タプル: ()
- 辞書：{}
- いずれにしても、角括弧を使えば単一の要素にアクセスできる(リスト、タプルはオフセット、辞書はキー)

## 3.7 もっと大きいデータ構造
- Sample: タプルをキーにして、作ったGPS座標の辞書
    ```python
    >>> house = {
    ... (44.79, -93.14, 285): 'My House',
    ... (38.89, -77.03, 13): 'The White House'
    ... }
    >>> house
    {(44.79, -93.14, 285): 'My House', (38.89, -77.03, 13): 'The White House'}
    ```