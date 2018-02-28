# 5.4 パッケージ
'''
同じ階層ディレクトリにweatherというディレクトリをパッケージとして作成し、
daily.py、weekly.pyを作成した。
そして、Pythonに当ディレクトリがパッケージだと認識させるため、
__init__.py（中身は空でよい）をディレクトリへ追加
（なくても無事実行できそう）
'''
from weather import daily, weekly

print('Daily forecast:', daily.forecast())

print('Weekly forecast:')
# enumerate()：インデックス付きのenumerateへ変換する
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)
