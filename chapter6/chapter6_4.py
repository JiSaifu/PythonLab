import chapter6_2
# 6.4 メソッドのオーバーライド


class Car:
    @staticmethod
    def exclaim():
        print("I'm a car!")


class Yugo(Car):
    @staticmethod
    def exclaim():
        print("I'm a Yugo! Much like a Car, but more Yugo-ish")


give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
give_me_a_yugo.exclaim()


class MDPerson(chapter6_2.Person):
    # __init()__含むあらゆるメソッドをオーバーライドできる。
    def __init__(self, name):
        self.name = 'Doctor ' + name


doctor = MDPerson('Fudd')
print(doctor.name)
