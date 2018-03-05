# 8.2 構造化されたテキストファイル
import csv  # for 8.2.1
import xml.etree.ElementTree as et  # for 8.2.3
import json # for 8.2.4
import datetime # for 8.2.4
from time import mktime # for 8.2.4
import configparser # 8.2.7

# 8.2.1 CSV
print('--- 8.2.1 ---')
villains = [['Doctor', 'No'], ['Rosa', 'Klebb'], ['Mister', 'Big'], ['Auric', 'Goldfinger'], ['Ernst', 'Blofeld']]

# windowsの場合、open関数にnewline=''を渡し、改行をCSVモジュールに任せる。
with open('villains', 'wt', newline='') as fout:
    csvout = csv.writer(fout)
    csvout.writerows(villains)
with open('villains', 'rt') as fin:
    cin = csv.reader(fin)   # reader()はリストのリストとしてデータを読み出す。
    villains = [row for row in cin]
print(villains)

with open('villains', 'rt') as fin:
    '''
    DictReader()はリストのリストではなく、辞書のリストとしてデータを読み出す。
    ・ fieldnames:ヘッダーの名前を指定できる。（省略すると、最初の列の値でヘッダーとして使われる）
    ・ Python3.6から、返される列の型はOrderedDictになる。（教科書と違うところ）
    '''
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin]
print(villains)

with open('villains', 'wt', newline='') as fout:
    '''
    DictWriter()はヘッダー付きのCSVファイルを書き込むことができる
    DictWriter(file, fieldnames)
    ※ fieldnamesは書き込み対象Dictのキーとマッチしないと、エラーになる。
    '''
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    # writerrows()の書き込み対象は必ずキーを持つオブジェクトでないとならない。
    cout.writerows(villains)

# 8.2.2 XML
# PythonでXMLを最も簡単に読み取るために、ElementTreeを使えばいい。
# また、xml.dom, xml.saxとのライブライも使える。
print('--- 8.2.2 ---')
tree = et.ElementTree(file='books.xml')
root = tree.getroot()
print(root.tag)

for child in root:
    print('tag:', child.tag, 'attribute:', child.attrib)
    for grandchild in child:
        print('\ttag:', grandchild.tag, 'attribute:', grandchild.text)
print(len(root))
print(len(root[0]))

# 8.2.4 JSON
menu = \
    {
        "breakfast": {
            "hours": "7-11",
            "items": {
                "breakfast burritos": "$6:00",
                "pancakes": "$4.00"
            }
        },
        "lunch": {
            "hours": "11-3",
            "items": {
                "hamburger": "$5:00"
            }
        }
    }

menu_json = json.dumps(menu)
print(menu_json)

menu2 = json.loads(menu_json)
print(menu2)

# 8.2.7 設定ファイル
cfg = configparser.ConfigParser()
# 設定ファイルは必要に応じてencodingを設定する
cfg.read('setting.cfg', encoding='UTF8')
print(cfg)
print(cfg['french'])
print(cfg['french']['greeting'])
print(cfg['common']['greeting'])
print(cfg['files']['bin'])

