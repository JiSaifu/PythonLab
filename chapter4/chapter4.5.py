# 4.5 forによる反復処理
print('--- 4.5 ---')
# Pythonのイテラブル（イテレータに対応している）プロジェクト：
# リスト、文字列、タプル、辞書、集合、その他

# 文字列をforで処理すると、一度に1字ずつ文字が生成される。
word = 'cat'
for letter in word:
    print(letter)

# 辞書（または辞書のkeys関数）をforで処理すると、キーが返される。
accusation = {'room': 'ballroom', 'weapon': 'pipe', 'person': 'Col. Mustard'}
for card in accusation:# または for card in accusation.keys():
    print(card)
# keyではなく、値が返されたい場合、辞書のvalues()関数を使えばよい。
for value in accusation.values():
    print(value)
# keyと値の両方をタプルの形で返したい場合には、items()関数を使う。
for item in accusation.items():
    print(item)
# タプルの各要素を個別の変数に代入する作業は、ワンステップでできる。
for card, content in accusation.items():
    print('Card', card, 'has the contents', content)

# 4.5.3 elseによるbreakのチェック
print('--- 4.5.3 ---')
# breakが呼び出されなければ、else文が実行される
cheeses = ['meiji']
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:
    print('This is not much of a cheese shop, is it?')

# 4.5.4 zip()を使った複数のシーケンスの反復処理
# zip()関数を使えば、複数のシーケンスを並列的に反復処理できる
print('--- 4.5.6 ---')
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
# zip()は、もっともサイズの小さいシーケンスの要素を処理しつくしたときにとまる
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruits, dessert in zip(days, fruits, desserts):
    print(day, ": eat", fruits, "- enjoy", dessert)

# zipを使えば、複数のシーケンスをたどって、オフセットが共通する要素からタプルを作ることができる
# zipから返すのはイテラブルな値で、list、tuple、dictなどで変換する必要がある
english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'
print(list(zip(english, french)))
print(tuple(zip(english, french)))
print(dict(zip(english, french)))

# 4.5.5 range()による数値シーケンスの生成
# range()は、range([start], end, [step])というスライスとよく似た形式で使う
# startを省略すると、0が先頭になる。
# 唯一の必須引数はendで、スライスと同様に、作成された最後の値はstopの直前である。
# stepのデフォルト値は1だが、-1を指定して逆順にすることができる。
# range()はイテラブルなオブジェクトを返すので、戻り値はfor...inで反復処理するか、
# リストなどのシーケンスに変換する必要がある

for x in range(0, 3):
    print(x)
print(list(range(0, 3)))
print(tuple(range(1, 11, 2)))
# 以下のstepは必ずマイナスにする
print(list(range(2, -1, -1)))





