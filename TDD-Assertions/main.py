from calc import soma

try:
    print(soma(1,'2'))

except AssertionError as e:
    print('Error: ', e)