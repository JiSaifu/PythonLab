# 4.12 独自例外の作成
'''
Pythonの例外もJavaと同じクラスで定義する。
クラスに関して、chapter6で深入る。
'''
class UppercaseException(Exception):
    pass # 処理内容はなくても、passを使ってほしい

words = ['eeenie', 'meenie', 'miny']
for word in words:
    if word.isupper(): # isupper()のチェック内容：チェック対象文字列はすべて大文字か
        raise UppercaseException(word)

class OopsException(Exception):
    pass

try:
    raise OopsException('panic')
except OopsException as exc:
    print(exc)