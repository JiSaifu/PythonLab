# 6.8 プロパティによる属性値の取得、設定
# ※Pythonでは、すべての属性とメソッドは公開であり、プログラマーが行儀よくふるまうのが前提になる。


class Duck:
    def __init__(self, input_name, input_age):
        self.hidden_name = input_name
        self.hidden_age = input_age

    def get_name(self):
        print('inside the getter(name)')
        return self.hidden_name

    def set_name(self, input_name):
        print('inside the setter(name)')
        self.hidden_name = input_name
    # property()にget、setメソッドを定義すると、外部からプロパティをアクセスする場合、
    # get、setメソッドを自動的に呼出す。
    name = property(get_name, set_name)

    '''
    プロパティは、デコレータで定義することもできる。
        ・ @property
            ゲッターメソッドの前に付けるデコレータ
        ・ @属性名.setter
            セッターメソッドの前に付けるデコレータ
    '''
    @property
    def age(self):
        print('inside the getter(age)')
        return self.hidden_age

    @age.setter
    def age(self, input_age):
        print('inside the setter(age)')
        self.hidden_age = input_age


fowl = Duck('Howard', 16)
print(fowl.hidden_name)

fowl.name = 'Daffy'
print(fowl.name)
print(fowl.get_name())

fowl.age += 1 # ここでageのgetメソッドは先に呼出されて、計算を行い、またsetメソッドを呼出す。
print(fowl.age)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    '''
    プロパティは単純な属性参照/設定ではなく、一定の処理をされた後の値として参照することもできる。
    diameterは属性と同じく参照できるが、設定用デコレータが実装されていないため、値の設定はできない。
    読み出し専用のプロパティとして作られている。
    '''
    @property
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
print(c.radius)
print(c.diameter)

