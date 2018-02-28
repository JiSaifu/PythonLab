# 4.10 名前空間とスコープ

# グローバル変数（グルーバル名前空間）
animal = 'fruitbat'
def print_global():
    # グルーバル変数の値は、関数内から参照できる。
    print('inside print_gobal:', animal)

print('at the top level:', animal)

# グルーバル変数を下記のように関数内から修正すると、エラーになる。
# def change_and_print_global():
    # print('inside change_and_print_global:', animal)
    # animal = 'wombat'
    # print('after the change:', animal)

def change_local():
    # 関数内で定義するanimalは関数のローカル名前空間内の存在
    animal = 'wombat'
    # id()はPythonから個々のオブジェクトに与えられた一意な値を表すもの。
    # これで関数内のanimalのidとグルーバル変数のidは違うことが分かれる。
    print('inside change_local:', animal, id(animal))

    # locals(): ローカル名前空間の内容を示す辞書を返す
    print('locals:', locals())

change_local()

print(animal, id(animal))

# 関数内からグローバル変数の方にアクセスするには、globalキーワードを使う。
# （書かなければローカル変数として扱い、関数が終わったら、ローカル変数は消えてなくなる）
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)

change_and_print_global()
print(animal)

print('globals:')
# globals(): グローバル名前空間の内容を示す辞書を返す
global_args = globals()
for global_arg in list(global_args.items()):
    print(global_arg)

# 4.10.1 名前のなかの_と__
print('--- 4.10.1 ---')
'''
先頭と末尾が2個のアンダースコア（_）になっている名前は、Pythonが使う変数として予約されている。
globals()の内容からもわかるように、メインプログラムには__main__という特別な名前が与えられている。
'''
