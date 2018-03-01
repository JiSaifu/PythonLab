# 6.14 名前付きタプル
"""
JavaとObject.equals, cloneと似ていて、Pythonのクラスにも特殊な上書きできるメソッドがある。
特殊なメソッドをカスタマイズで定義すれば、対応する式を直接使えばいろんな機能が便利に利用できる
参考：
http://omake.accense.com/static/doc-ja/cython/src/reference/special_methods_table.html
"""

from collections import namedtuple

'''
namedtuple()引数：
    ・ 名前
    ・ 空白区切りおフィールド名の文字列
'''
Duck = namedtuple('Duck', 'bill tail test')
duck = Duck('wide orange', 'long', 'test')
print('duck:', duck)
print('duck.bill:', duck.bill)
print('duck.tail:', duck.tail)

parts = {'bill': 'wide orange', 'tail': 'long', 'test': 'test'}
duck2 = Duck(**parts)
print('duck2:', duck2)

duck3 = duck2._replace(tail='short')
print('duck3:', duck3)
