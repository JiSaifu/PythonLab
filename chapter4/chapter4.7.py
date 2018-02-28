# 4.7 関数
# 文法：def function_name(parameter1, parameter2...):
# （関数名の先頭は英字か“_”でなければならず、英数字、_以外使えない）

# 4.7.1 位置引数
print('--- 4.7.1 ---')
def menu(wine, entree, dessert):
    return {'wine':wine, 'entree':entree, 'dessert':dessert}

print(menu('chardonnay', 'chicken', 'cake'))

# 4.7.2 キーワード引数
print('--- 4.7.2 ---')
# 位置引数の混乱を避けるには、対応する仮引数の名前を指定して実引数を指定すればよい。
print(menu(wine='bordeaux', entree='beef', dessert='bagel'))
# 位置引数とキーワード引数を併用する場合、まず先に位置引数を指定しなければならない。
print(menu('frontenac', entree='fish', dessert='flan'))

# 4.7.3 デフォルト引数値の指定
print('--- 4.7.3 ---')
def menu_def(wine, entree, dessert='pudding'):
    return {'wine':wine, 'entree':entree, 'dessert':dessert}
print(menu_def('chardonnay', 'chicken'))
# 引数を指定すれば、それがデフォルト値の代わりに使われる
print(menu_def('chardonnay', 'chicken', 'doughnut'))

# デフォルト引数の値が計算されるのは、関数が実行されたときではなく
# 定義された時だ。
# 下記2回目に呼び出されたとき、
# resultには前回の呼び出しでセットされた1個の要素がまだ残っている
def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a')
buggy('b')

# 修正後：
def nonbuggy(arg, result=None):
    # 引数を指定しなければ、Noneになる
    if result == None :
        result = []
    result.append(arg)
    print(result)
nonbuggy('a')
nonbuggy('b')

# 4.7.4 *による位置引数のタプル化
print('--- 4.7.4 ---')
# args:仮引数をargsに呼ぶ必要は特にないが、Pythonコミュニティでは一般的な慣習となる。
def print_args(*args):
    print('Positional argument tuple:', args)
print_args()
print_args(3, 2, 1, 'wait!', 'uh...')

'''
必須の位置引数がある場合は、位置引数の最後に*argsを書くと、
必須引数以外のすべての位置引数を一つにまとめることができる
逆に下記のような書き方で書くと必須引数の名前を指定しなければならない。
'''
def print_more(require1, *args, require2):
    print('require1: ' + str(require1) + ' require2: ' + str(require2))
    print(args)
print_more(1, 2, 3, 4, require2=5)

# 4.7.5 **によるキーワード引数の辞書化
# 引数を辞書化にする
print('--- 4.7.5 ---')
'''
位置引数を纏める*argsと**kwargsを併用する場合、この二つはこの順序で、
並べなければならない（逆にするとコンパイルエラーになる）。この引数を、
kwargsと呼び必要はないが、一般にこの名前を使われている。
'''
def print_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

print_kwargs(1, 2, 3, 4, 5, a=2, b=3)

# 4.7.6 docstring
print('--- 4.7.6 ---')
# 関数の説明ドキュメントを定義する
def print_if_true(thing, check):
    # request方式のコメントの書き方だが、具体的な文法は要確認
    '''
    第二引数が真なら、第一引数を表示する
    処理内容：
        1.*第二*引数が真かどうかをチェックする
        2.真なら*第一*引数を表示する
    :param thing: 表示対象
    :param check: 表示対象を表示するかどうかの条件
    :return: なし
    '''
    if check:
        print(thing)

print_if_true("HaHa", True)
# 綺麗な整形されたdocstringが返される
help(print_if_true)
# 整形前の素のままのdocstringを見たい場合には、次のようにする
help(print_if_true.__doc__)

# 4.7.7 一人前のオブジェクトとしての関数
print('--- 4.7.7 ---')
# Pythonでは、関数もオブジェクトだ
def add_args(arg1, arg2):
    print(arg1 + arg2)
    return arg1 + arg2

def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)

'''
funcに渡したのはadd_args(...)ではなく、add_argsだ
Pythonではこの括弧は関数呼び出しを意味する。括弧がなければ、
Pythonは関数をほかのオブジェクトと同じよう扱う。
'''
run_something_with_args(add_args, 1, 2)

def sum_args(*args):
    print(type(args))
    return sum(args)

def run_with_positional_args(func, *args):
    # func(args)で実装すると、ランタイムエラーになる
    return func(*args)

print(run_with_positional_args(sum_args, add_args(1, 2), 3, 4))

# 4.7.8 関数内関数
print('--- 4.7.8 ---')
# 関数内関数は、ループやコードの重複を避けるために役に立つ。
def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

print(knights('Ni'))

# 4.7.9 クロージャ-Closure
print('--- 4.7.9 ---')
'''
クロージャとは、ほかの関数によって動的に生成される関数で、
その関数の外で作られた変数の値を覚えておいたり、変えたりすることができる。
'''
def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2
a = knights2("Duck")
b = knights2("Hasenpfeffer")
print(type(a), type(b))
print(a, b)
'''
二つのクロージャはknight2に自分たちが作られたときに使われていたsayingの内容を覚えている
'''
print(a(), b())

# 4.7.10 無名関数：ラムダ関数
# Pythonでは、ラムダ関数は一つの文で表現される無名関数だ。
print('--- 4.7.10 ---')
def edit_story(words, arg2, func):
    for word in words:
        print(func(word, arg2))
stairs = ['thud', 'meow', 'thud', 'hiss']
def enliven(word):
    return word.capitalize() + '!'

'''
下記ラムダは2つの引数を取り、ここではそれをword, arg2と呼んでいる（ではなくても大丈夫）。
コロンから括弧までの部分は、すべて関数定義である。
'''
edit_story(stairs, 'arg2', lambda word, arg2: word.capitalize() + arg2)