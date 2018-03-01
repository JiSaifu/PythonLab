# 6.13 コンポジション
"""
JavaとObject.equals, cloneと似ていて、Pythonのクラスにも特殊な上書きできるメソッドがある。
特殊なメソッドをカスタマイズで定義すれば、対応する式を直接使えばいろんな機能が便利に利用できる
参考：
http://omake.accense.com/static/doc-ja/cython/src/reference/special_methods_table.html
"""


class Bill:
    def __init__(self, description):
        self.description = description

class Tail:
    def __init__(self, length):
        self.length = length

class Duck:
    def __init__(self, bill, tail):
        self.bill = bill
        self.tail = tail

    def about(self):
        print('This duck has a',
              self.bill.description, 'bill and a',
              self.tail.length, 'tail')


tail = Tail('long')
bill = Bill('wide orange')
duck = Duck(bill, tail)
duck.about()
