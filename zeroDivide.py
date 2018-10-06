def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('エラー：不正な引数です')


print(spam(10))
print(spam(0))