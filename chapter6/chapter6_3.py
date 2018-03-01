# 6.3 継承
class Car:

    def exclaim(self):
        print("I'm a car!")


class Yugo(Car):
    '''
    サブクラスは、同じclassキーワードを使って定義するが、
    括弧内に親クラスの名前を入れる。
    '''
    pass


give_me_a_car = Car()
give_me_a_yogo = Yugo()
give_me_a_car.exclaim()
give_me_a_yogo.exclaim()

'''
＜6.7　selfの自己弁護＞の内容だが、
メソッドを呼び出す際に、self引数を渡せなければならない。
give_me_a_car.exclaim()の呼出す方法があるが、
下記のようなやり方（結果は一緒、ただあえて使う理由はない）もある。
'''
Car.exclaim(give_me_a_car)
