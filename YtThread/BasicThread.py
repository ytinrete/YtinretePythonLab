import threading


def test_thread():
    print('lalala')


if __name__ == '__main__':
    threading.Thread(target=test_thread).start()
