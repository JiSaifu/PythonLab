# 2.2 数値

# 2.2.1 整数
print('--- 2.2.1 ---')
# 特殊な算術演算子
# // 整数の除算（切り捨て） 例：7 // 2 = 3
# ** 指数 例： 3 ** 4 = 81

# Javaと同じ、変数を計算した後に再代入する場合
a = 3
a -= 1
print(a)

# 整数の先頭に0をおいてはならない

# 商と剰余を同時に取得
print(divmod(9, 5))

# 2.2.3 基数
print('--- 2.2.3 ---')
# 十進数
print(10)
# 二進数
print(0b10)
# 八進数
print(0o10)
# 十六進数
print(0x10)
print(0xf)

# 2.2.4 型の変換
print('--- 2.2.4 ---')
print(int(True))
print(int(False))

# 整数に変換する場合、小数点以下の部分が単純に切り捨てられる
print(int(98.6))
print(int('+11'))
print(int('-11'))
print(int(10.1e4))

# 整数変換の場合、小数点や指数部を含む文字列が処理できない
# print(int('98.1')). print(int('10e4'))

# 2.2.5 intはどれぐらい大きいのか
# Python2: -2147483648~2147483647(32bit, longは64bit)
# Python3: 任意

# 2.2.6 浮動小数点数
print('--- 2.2.6 ---')
print(float(True))
print(float(False))
print(float(98))
print(float('99.9') // 10)
print(float('99.9') % 10)
