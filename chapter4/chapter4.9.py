# 4.9 デコレータ
# ある関数を修飾するための関数とその仕組み。
def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Key arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function

def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function

'''
関数に最も違いデコレータ(defのすぐ上）が先に実行され、次にその上のデコレータが実行される。
以下の例としては、square_itが先に実行され、resultは64になる。
その後document_itが実行され、resultはsquare_itに処理されたものを出力される。
'''
@document_it
@square_it
def add_ints(a, b):
    return a + b

print(add_ints(3, 5))
