# 4.11 エラー処理とtry、except

short_list = [1, 2, 3]
position = 5
try:
    print(short_list[position])
except:
    print('Need a position between 0 and', len(short_list) - 1,
          ',but got', position)
print('after try-except block...')

while True:
    value = input('Position [q to quit]?')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
        # Javaと同じく、もっと細かく限定された例外はもっと前に書く。
    except IndexError as err: # except exception_type as name
        print('Bad Index', position)
    except Exception as other:
        print('Something else broke:', other)
        # Javaのthrowと似ている、ただthrowsはなさそう。
        raise other
