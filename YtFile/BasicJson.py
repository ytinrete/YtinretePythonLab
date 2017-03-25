import json


def read(str):
    try:
        obj = json.loads(str)
        for (k, v) in obj.items():
            print('key:' + k, ' value:' + v)
        return obj
    except BaseException as e:
        print(e)


def write(obj):
    str = json.dumps(obj)
    print(str)
    return str


if __name__ == '__main__':
    str = '{"foo":"test", "bar":"123"}'
    write(read(str))
    pass
