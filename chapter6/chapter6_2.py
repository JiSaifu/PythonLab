# 6.2 classによるクラスの定義
class Person():
    # 空クラス定義するのは、passが必要である。
    # pass

    '''
    __init__(): オブジェクトを初期化する特殊なメソッド　※必須ではない
        第一引数はオブジェクト自体を参照するパラメータでなければならない、
        通常引数名は"self"である。
    '''

    def __init__(self, name):
        self.name = name


hunter = Person('Elmer Fudd')
print('The mighty hunter: ', hunter.name)
