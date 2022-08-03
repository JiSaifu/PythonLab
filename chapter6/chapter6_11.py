# 6.11 ダックタイピング(Duck Typing：鴨子类型)
'''
Pythonは、ポリモーフィズムの緩やかな実装を持っている。
クラスの種類にかかわらず、異なるオブジェクトに対して同じ操作を適用するのである。
'''

class Quote:
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + '.'


class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'


class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


class BabblingBrook:
    @staticmethod
    def who():
        return 'Brook'

    @staticmethod
    def says():
        return 'Babble'


def who_says(obj):
    '''
    ダックタイピングは動作が属するクラスに要求しないが、動作自体だけ注目する。
    なので、下記のobjはどんなクラスになってもいいが、whoとsaysだけ、これを使うクラスに実装されなければならない。
    '''
    print(obj.who(), 'says', obj.says())


who_says(Quote('Elmer Fudd', "I'm hunting wabbits"))
who_says(QuestionQuote('Bugs Bunny', "What's up, doc"))
who_says(ExclamationQuote('Daffy Duck', "It's rabbit season"))
who_says(BabblingBrook())
