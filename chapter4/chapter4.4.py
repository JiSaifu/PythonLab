# 4.4 whileによる反復処理
print('--- 4.4 ---')
count = 1
while count <= 5:
    print(count)
    count += 1

# 4.4.1 breakによるループの中止
print('--- 4.4.1 ---')
while True:
    stuff = input("String to capitalize [type q to quit]:")
    if stuff == 'q':
        break
    print(stuff.capitalize())

# 4.4.2 continueによる次のイテレーションの開始
while True:
    value = input("Integer, please[q to quit]:")
    if value == 'q':
        break

    number = int(value)
    if number % 2 == 0:# 偶数
        continue
    print(number, "squared is", number * number)
# 4.4.3 elseによるbreakのチェック
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:
    # breakが呼び出されない場合、else配下の処理が実行される
    # 当例で偶数が存在し、breakが呼び出されると、else配下の処理が呼び出されない
    print('No even number found')