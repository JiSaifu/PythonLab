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





