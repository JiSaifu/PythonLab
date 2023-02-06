# 4章 Pythonの皮：コード構造
- チェックポイント
    - [4.4.3 elseによるbreakのチェック](#443-elseによるbreakのチェック)

---
## 4.1 #によるコメント
- #によるコメントをつける
- 複数行コメントはない。コメントセクションの冒頭に#をつける必要がある

## 4.2 \による行の継続
- 行が長すぎると読みにくいので、継続文字の\を使う
``` python
>>> 1 + 2 + \
... 3
6
>>> alphabet = "abcdefg" + \
... "hijklmn"
>>> alphabet
'abcdefghijklmn'
```
## 4.3 if、elif、elseによる比較
- ifテストでかっこはいらない；末尾にセミコロン:が必要
- サブセクションのインデントのために4文字（推奨）のスペース/タブを使う
``` python
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
Woe!
print("out of if block")
out of if block
```

- テスト結果が3種類以上に分かれる場合、if、elif、elseを使う
``` python
>>> color = "puce"
>>> if color == "red":
...     print("It's a tomato")
... elif color == "green":
...     print("It's a green pepper")
... elif color == "bee purple" :
...     print("I don't know what it is, but only bees can see it")
... else:
...     print("I've never heard of the color", color)
... 
I've never heard of the color puce
```
- Pyの比較演算子

    意味|演算子
    ---|---
    等しい|==
    等しくない|!=
    要素になっている|in ...

- ブール演算子: and, or, not
    - ブール演算子は比較対象の要素よりも優先順位が低い

- 1個の変数で複数の比較をandする場合、次のように書くことができる
``` python
>>> x = 7
>>> print(5 < x < 10 < 999)
True
>>> print(5 < x < 10 > 999) 
False
```

### 4.3.1 Trueとは何か
- Pythonは必ずしも明示的にFalseである必要はない。
    - Falseとみなされるもの
    
    Falseとみなされるもの|値
    ---|---
    ブール値|False
    null|None
    整数のゼロ|0
    floatのゼロ|0.0
    空文字列|''
    空リスト|[]
    空タプル|()
    空辞書|{}
    空集合|set()
``` python
>>> if some_list: 
...     print("There's something in here")
... else:
...     print("Hey, it's empty!")
... 
Hey, it's empty!
```
## 4.4 whileによる反復処理
``` python
>>> count = 1
>>> while count <= 5:
...     print(count)
...     count += 1
... 
1
2
3
4
5
```

### 4.4.1 breakによるループの中止
``` python
>>> while True:
...     stuff = input("String to capitalize [type q to quit]:")
...     if stuff == 'q':
...         break
...     print(stuff.capitalize())
... 
String to capitalize [type q to quit]:aaa
Aaa
String to capitalize [type q to quit]:q
```

### 4.4.2 continueによる次のイテレーション (Iteration) の開始
``` python
>>> while True:
...     value = input("Integer, please[q to quit]:")
...     if value == 'q':
...         break
...     number = int(value)
...     if number % 2 == 0:# 偶数
...         continue
...     print(number, "squared is", number * number)
... 
Integer, please[q to quit]:1
1 squared is 1
Integer, please[q to quit]:2
Integer, please[q to quit]:3
3 squared is 9
```

### 4.4.3 elseによるbreakのチェック
- breakが呼び出されない場合、else配下の処理が実行される
- break中の内容が実行されたか、つまりbreakチェッカーと考えるとよい
``` python
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:
    # 当例で偶数が存在し、breakが呼び出されると、else配下の処理が呼び出されない
    print('No even number found')

No even number found
```

## 4.5 forによる反復処理
- Pythonのイテラブル（イテレータに対応している）プロジェクト：リスト、文字列、タプル、辞書、集合、その他
    - 文字列をforで処理すると、一度に1字ずつ文字が生成される。
    ``` python
    word = 'cat'
    for letter in word:
        print(letter)
    ... 
    c
    a
    t
    ```

    - 辞書（または辞書のkeys関数）をforで処理すると、キーが返される。
    ``` python
    accusation = {'room': 'ballroom', 'weapon': 'pipe', 'person': 'Col. Mustard'}
    for card in accusation:# または for card in accusation.keys():
        print(card)
    ... 
    room
    weapon
    person
    ```
    - keyではなく、値が返されたい場合、辞書のvalues()関数を使えばよい。
    ``` python
    for value in accusation.values():
        print(value)
    ... 
    ballroom
    pipe
    Col. Mustard
    ```
    - keyと値の両方をタプルの形で返したい場合には、items()関数を使う。
    ``` python
    for item in accusation.items():
        print(item)
    ... 
    ('room', 'ballroom')
    ('weapon', 'pipe')
    ('person', 'Col. Mustard')
    ```
    - タプルの各要素を個別の変数に代入する作業は、ワンステップでできる。
    ``` python
    for card, content in accusation.items():
        print('Card', card, 'has the contents', content)
    ... 
    Card room has the contents ballroom
    Card weapon has the contents pipe
    Card person has the contents Col. Mustard
    ```
### 4.5.3 elseによるbreakのチェック
- whileのelseと同様に、for中のbreakが実行されていなければ、elseの内容が実行される(そもそもbreak文がない場合も、elseが実行される)
``` python
>>> cheeses = ['meiji']
>>> for cheese in cheeses: 
...     print('This shop has some lovely', cheese)
...     break
... else:
...     print('This is not much of a cheese shop, is it?')
... 
This shop has some lovely meiji
```

### 4.5.4 zip()を使った複数のシーケンスの反復処理
- zip()関数を使えば、複数のシーケンスを並列的に反復処理できる
- zip()は、もっともサイズの小さいシーケンスの要素を処理しつくしたときにとまる
``` python
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
# dessertsは4つの要素があるが、他のリストより多い分「pudding」は取り出されない
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, dessert in zip(days, fruits, desserts):
    print(day, ": eat", fruit, "- enjoy", dessert)
... 
Monday : eat banana - enjoy tiramisu
Tuesday : eat orange - enjoy ice cream
Wednesday : eat peach - enjoy pie
```
- zipを使えば、複数のシーケンスをたどって、オフセットが*共通する*要素からタプルを作ることができる
- zipから返すのは*イテラブルな値*で、list、tuple、dictなどで変換する必要がある
``` python
>>> english = 'Monday', 'Tuesday', 'Wednesday', 'Thursday'
>>> french = 'Lundi', 'Mardi', 'Mercredi'
>>> zip(english, french)
<zip object at 0x000002134F1FD100>
>>> list(zip(english, french))
[('Monday', 'Lundi'), ('Tuesday', 'Mardi'), ('Wednesday', 'Mercredi')]
```

### 4.5.5 range()による数値シーケンスの生成
- コンピュータのメモリを使い尽くしてプログラムをクラッシュさせたりせずに、非常に大きな範囲の数値を作ることができる
- range()は、range([start], end, [step])というスライスとよく似た形式で使う
    - startを省略すると、0が先頭になる。
    - 唯一の必須引数はendで、スライスと同様に、作成された最後の値はstopの直前である。
    - stepのデフォルト値は1だが、-1を指定して逆順にすることができる。
- range()はイテラブルなオブジェクトを返すので、戻り値はfor...inで反復処理するか、リストなどのシーケンスに変換する必要がある
``` python
>>> for x in range(0, 3):
...     print(x)
... 
0
1
2
>>> print(list(range(0, 3)))
[0, 1, 2]

>>> print(tuple(range(1, 11, 2)))
(1, 3, 5, 7, 9)

# 以下のstepは必ずマイナスにする
>>> print(list(range(4, -1, -1)))
[4, 3, 2, 1, 0]
```