def test():
    return 'Hello World!'

if __name__ == '__main__':#直接yobareru.pyを実行した時だけ、def test()を実行する
    test()

print('モジュール名：{}'.format(__name__))  #実行したモジュール名を表示する