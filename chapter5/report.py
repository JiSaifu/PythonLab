'''呼出されるモジュール'''

# 5.3.1 モジュールのインポート
def get_description():
    '''プロと同じようにランダムな天気を返す'''
    # importされるコードが複数の関数で使われる場合、外でインポートする
    # 使われる場所が1つの関数に限定されている場合には、使う関数の中から呼出す。

    # ほかのchoiceという名前のものはないことがわかっているので、
    # randomモジュールから直接choice関数をインポートできる。
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)
