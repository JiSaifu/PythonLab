# 5.3 モジュールとimport文
'''
モジュール：Pythonコードを纏めたファイルである。
import：importしたほかのモジュールのコード、変数をプログラム内で使えるようになる。

備考：IntelliJよりエラーなしインポートさせる方法として、
Project StructureのLibrary設定にインポート対象が存在されるパスを追加する必要。
'''

# 5.3.1 モジュールのインポート
def func_3_1():
    print('--- 5.3.1 ---')
    # ここでmoduleの部分は、ほかのPythonファイルのファイル名から拡張子の.pyを取り除いたものである。
    # report.pyは同じディレクトリに置かれる必要がある。
    import report
    # reportとのプレフックスを使わなければならない。（名前の衝突が避けられる）
    description = report.get_description()
    print("Today's weather:", description)

# 5.3.2 別名によるモジュールのインポート
def func_3_2():
    print('--- 5.3.2 ---')
    '''
    同じ名前の別のモジュールが必要な時や、
    もっと覚えやすい名前や簡潔な名前を使いたい場合、別名を使ってインポートする
    '''
    import report as wr
    description = wr.get_description()
    print("Today's weather:", description)

# 5.3.3 必要なものだけをインポートする方法
def func_3_3():
    print('--- 5.3.3 ---')
    '''
    モジュールから一つ以上の部品だけをインポートすることができる。
    もとの名前にするか別名を使うかは部品ごとに決められる。
    '''
    # もとの名前でインポートする
    from report import get_description
    print("Today's weather:", get_description())

    # 別名(do_it)でインポートする
    from report import get_description as do_it
    print("Today's weather:", do_it())

# 5.3.4 モジュールサーチパス
def func_3_4():
    # インポートするファイルの検索パス⇒sys.path
    print('--- 5.3.4 ---')
    import sys
    for place in sys.path:
        print(place)
    '''
    カレントディレクトリから検索する。
    インポートされるのは最初にマッチしたファイルだ。
    例えば、自分はrandomというモジュールをカレントディレクトリに定義したら、
    インポートするのは自分で定義したもので、標準ライブラリのrandomはインポートできない。
    '''

func_3_1()
func_3_2()
func_3_3()
func_3_4()
