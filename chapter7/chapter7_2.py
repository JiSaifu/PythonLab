# 7.2.2用モジュール
import struct
# 7.2.4用モジュール
import binascii
# 7.2 バイナリデータ
# 7.2.1 バイトとバイト列
'''
Python 3は、0から255までの値を取る8ビット整数の2種類のシーケンスを導入した。
・bytesはイミュータブルで、バイトのタプルのようなものだ。
・bytearrayはミュータブルで、バイトのリストのようなものだ。
'''
print('--- 7.2.1 ---')
blist = [1, 2, 0xf, 255]
# 0-255（超えるとエラーになる）の整数値（16進数を直接に使ってもOK）でbytes/bytearrayを設定する
the_bytes = bytes(blist)
print(the_bytes)

the_bytes_array = bytearray(the_bytes)
print(the_bytes_array)
the_bytes_array.append(0xff)
print(the_bytes_array)

'''
bytes/bytearrayデータを表示するとき、Pythonは印字不能バイトについては\\xxx形式を使い、
印字可能バイトはASCII文字を表示する（\\n、\\rとかも含め）
'''
print(b'\x61')
the_bytes = bytes(range(0, 256))
the_bytes_array = bytearray(bytes(range(0, 256)))

print(the_bytes)

# 7.2.2 structによるバイナリデータの変換
print('--- 7.2.2 ---')
a = struct.unpack('>L', the_bytes[0:4])
b = struct.unpack('>L', the_bytes[4:8])
c, d = struct.unpack('>2L', the_bytes[0:8])
# 読み飛ばしをしてもいいが、すべてのバイトを処理しなけらばならない。(2+1+253=256)
e = struct.unpack('>2xB253x', the_bytes)
'''
x00x01x02x03　⇒　66051
x04x05x06x07　⇒　67438087
'''
print(a, b, c, d)
print(e)

# 7.2.4 binasciiによるバイト/文字列の変換
print('--- 7.2.4 ---')
print(binascii.hexlify(the_bytes))
print(binascii.unhexlify(binascii.hexlify(the_bytes)))

# 7.2.5 ビット演算子
print('--- 7.2.5 ---')
a = 0b0101
b = 0b0001
print('{0:04b} & {1:04b} = {2:04b}'.format(a, b, a & b))
print('{0:04b} | {1:04b} = {2:04b}'.format(a, b, a | b))
print('{0:04b} ^ {1:04b} = {2:04b}'.format(a, b, a ^ b))
print('~{0:04b} = {1:04b}'.format(a, ~a))
print('{0:04b} << 1 = {1:04b}'.format(a, a << 1))
print('{0:04b} >> 1 = {1:04b}'.format(a, a >> 1))
