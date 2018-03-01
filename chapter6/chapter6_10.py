# 6.10 メソッドのタイプ
'''
クラス定義の中でメソッドの第一引数がselfになっていたら、それはインスタンスメソッドだ。
呼出されるとPythonはメソッドにオブジェクトを与える
'''


class A:
    # クラス属性、すべてのオブジェクトに影響を与える（Javaのstatic属性らしい）
    count = 0

    def __init__(self):
        A.count += 1

    # クラスにも、オブジェクトにも影響を与えないメソッド(self, clsの参照も要らない)は、
    # staticmethodとして定義すればよい。
    @staticmethod
    def exclaim():
        print("I'm an A!")

    '''
    クラスメソッド（@classmethodのデコレータ）はクラス全体に影響を与える。
    クラスメソッドの第一引数は通常clsと命名される。
    '''
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")


easy_a = A()
breezy_a = A()
wheezy_a = A()

A.kids()
print(A.count)
print(easy_a.count)

# Javaと同じ、静的メソッドはクラスからオブジェクトを作らずに実行できる。
A.exclaim()
