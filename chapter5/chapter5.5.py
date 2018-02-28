# 5.5 Python標準ライブラリ
# 5.5.1 setdefault()とdefaultdict()による存在しないキーの処理
print('--- 5.5.1 ---')
periodic_table = {'Hydrogen':1, 'Helium':2}
print(periodic_table)

# setdefault(): keyがなければ、新しい値とともに辞書に追加される。
# ※set...との関数名だけど、dictから値を取得する機能
carbon = periodic_table.setdefault('Carbon', 12)
print(carbon)
print(periodic_table)

# 既存のキーに別のデフォルト値を代入しようとしても、元の値が返され、辞書は変更されない。
helium = periodic_table.setdefault('Helium', 947)
print(helium)
print(periodic_table)

# -------------------------------------------------
'''
defaultdict(): 辞書作成時にあらゆる新キーのためにあらかじめデフォルト値を設定する。
引数は関数である。引数を省略すると、デフォルト値にNoneが設定される。
'''
from collections import defaultdict
print(int())
# int()という形でdefaultdict()に呼出される。
periodic_table = defaultdict(int)
periodic_table['Hydrogen'] = 1
# 存在しないキーを用いた場合、そのキーが自動生成される。
print(periodic_table['Lead'])
print(periodic_table)

# デフォルト値生成用関数
def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
# 簡単なデフォルト値生成ロジックであれば、lambdaを使えばいい
# bestiary = defaultdict(lambda : 'Huh?')
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
print(bestiary['A'])
print(bestiary['B'])
print(bestiary['C'])

# 簡単な応用の例
food_counter = defaultdict(lambda : 0) # lambda : 0はint()と同じ結果を得られる
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)

# 5.5.2 Counter()による要素数の計算
print('--- 5.5.2 ---')
from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
print(breakfast_counter)

# most_common(): カウント結果を降順で返す
print(breakfast_counter.most_common())
# 引数として整数を指定すると、最上位から数えてその個数分だけを表示する
print(breakfast_counter.most_common(1))
print(breakfast_counter.most_common(100))

# カウンタの結合
lunch_counter = Counter(['eggs', 'eggs', 'bacon'])
print(breakfast_counter + lunch_counter)
print(breakfast_counter - lunch_counter)
print(lunch_counter - breakfast_counter)
# 積集合演算子の&を使えば、共通要素が得られる（カウンタは小さい方の値になる）
print(breakfast_counter & lunch_counter)
# 和集合演算子の|を使えば、全て要素が得られる（カウンタは大きい方の値になる）
print(breakfast_counter | lunch_counter)

# 5.5.3 OrderedDict()によるキー順のソート
print('--- 5.5.3 ---')
'''
辞書のキーの順序が予測不能だが、OrderedDict()を使えば、
キーが追加された順序と同じ順序でキーを返す
'''
from collections import OrderedDict
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!')
])

for k, v in quotes.items():
    print(k, v)

# 5.5.4 スタック（stack）＋キュー（queue）＝デック（deque）
'''
dequeは同時にstackとqueueの特性を持つ、
シーケンスのどちらの端でも要素の追加、削除できる
'''
print('--- 5.5.4 ---')
# 回文チェックの例：
def palindrome(word):
    from collections import deque
    dq = deque(word)
    dq.append('a')
    dq.appendleft('a')
    print(dq)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True
print(
    palindrome('a'),
    palindrome(''),
    palindrome('abcddcba'),
    palindrome('abcabcba'))

# 本chapterと関係ないが、実際に回文チェックをやる場合、下記のスライスでやる
def another_palindrome(word):
    return word == word[::-1]
print(another_palindrome('radar'), another_palindrome('hobbit'))

# 5.5.5 itertoolsによるコード構造の反復処理
'''
dequeは同時にstackとqueueの特性を持つ、
シーケンスのどちらの端でも要素の追加、削除できる
'''
print('--- 5.5.5 ---')
'''
itertoolsには、特別な目的を持つイテレータ関数が含まれている
for...in ループ内で呼出されると、一度に1個の要素を返し、
呼出しの間も自分の状態を覚えている
'''
import itertools

# chain()は、引数全体が一つのイテラブルであるかのように扱い、その中の要素を反復処理する。
# 例：[1, 2, 3], ['a', 'b'] ⇒ [1, 2, 3, 'a', 'b']
for item in itertools.chain([1, 2, 3], ['a', 'b']):
    print(item)

# cycle()は無限反復子で、引数から循環的に要素を返す。
# for item in itertools.cycle([1, 2]):
#     print(item)

# accumulate()は、要素を一つにまとめた値を計算する。デフォルトでは和を計算する。
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

'''
accmulate()は、第2引数として関数を受け付け、この引数が加算の代わりに使われる。
この関数は、2個の引数を受け付け、1個の結果を返すものでなければならない。
'''
def mulitply(a, b):
    return a * b
for item in itertools.accumulate([1, 2, 3, 4], mulitply):
    print(item)

# もちろん、上記の実装内容はlambdaでも実現できる
# for item in itertools.accumulate([1, 2, 3, 4], lambda a, b: a * b):
#     print(item)

# 5.5.6 pprint()によるきれいな表示
'''
pprint()は、読みやすくするために、要素の位置を揃えようとする。
'''
print('--- 5.5.6 ---')
from pprint import pprint
print(quotes)
pprint(quotes)