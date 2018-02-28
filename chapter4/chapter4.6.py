# 4.6 内包表記

# 4.6.1 リスト内包表記
print('--- 4.6.1 ---')
# 文法：[expression for item in iterable]
number_list = [number for number in range(1, 6)]
print(number_list)

number_list = [number-1 for number in range(1, 6)]
print(number_list)

# 内包表記に条件を追加
# 文法：[expression for item in iterable if condition]
a_list = [number for number in range(1, 6) if number % 2 == 1]
print(a_list)

rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row, col)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

for row, col in cells:
    print(row, col)

# 4.6.2 辞書包括表記
print('--- 4.6.2 ---')
# 文法：{key_item: value_item for item in iterable}
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)
print(set(word))
letter_counts = {letter: letter for letter in set(word)}
print(letter_counts)

# 4.6.3 集合内包表記
print('--- 4.6.3 ---')
# 文法：{item for item in iterator}
a_set = {number for number in range(1, 6) if number % 3 == 1}
print(a_set)

# 4.6.4 集合内包表記
print('--- 4.6.4 ---')
# 普通の括弧での内包表記：ジェネレータ内包表記
# イテレータにデータを供給する方法の一つである
number_thing = (number for number in range(1, 6))
print(number_thing)
print(type(number_thing))

for number in number_thing:
    print(number)

# ジェネレータはlist()関数でラッパすれば、
# リスト内包表記のように動作させることができる
number_list = list(number_thing)
print(number_list)
# ジェネレータは一度しか実行できない
number_thing = (number for number in range(1, 6))
number_list = list(number_thing)
print(number_list)
