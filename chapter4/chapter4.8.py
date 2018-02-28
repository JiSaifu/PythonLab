# 4.8 ジェネレータ
'''
役割：シーケンス全体を作ってメモリに格納しなくても、
（巨大になることがある）シーケンスを反復処理できる。

※rangeはPythonのバージョンによって動きは違う
・Python2: xrange()（range()はメモリに収まる以上のものを生成できない）
・Python3: range()
'''

def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

print(my_range)
print(my_range(1, 5))

for x in my_range(1, 5):
    print(x)