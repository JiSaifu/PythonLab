from pprint import pprint
# 6.12 特殊なメソッド（一部常用のもの）
"""
JavaとObject.equals, cloneと似ていて、Pythonのクラスにも特殊な上書きできるメソッドがある。
特殊なメソッドをカスタマイズで定義すれば、対応する式を直接使えばいろんな機能が便利に利用できる
参考：
http://omake.accense.com/static/doc-ja/cython/src/reference/special_methods_table.html
"""


class Word:
    def __init__(self, text):
        self.text = text


class WordEx(Word):
    def __eq__(self, word2):
        return self.text == word2.text


w1, w2 = Word('abc'), Word('abc')
wex1, wex2 = WordEx('abc'), WordEx('abc')
pprint((w1, w2))
print(w1 == w2)
print(wex1 == wex2)
