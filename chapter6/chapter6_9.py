# 6.9 非公開属性のための名前のマングリング(Mangling)


class Duck:
    def __init__(self, name):
        # Pythonは、クラス定義の外から見えないようにすべき属性の命名方法を持つ。
        # 先頭に二つのアンダースコア(__)を付ける
        self.__name = name

    @property
    def name(self):
        print('inside the getter(name)')
        return self.__name

    @name.setter
    def name(self, name):
        print('inside the setter(name)')
        self.__name = name


fowl = Duck('Howard')

# 下記のように、直接__nameをアクセスことができない。
# print(fowl.__name)
print(fowl.name)
fowl.name = 'Donald'
# ただし、この命名方法を使っても、非公開になるわけではないが、
# Pythonは、外部コードが偶然当てたりしないようなものに名前をマングリングする。
print(fowl._Duck__name)
# _Duck__name（マングリング）はgetメソッドを呼出さない。
