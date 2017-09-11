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


def write_to_file(file, obj):
    with open(file, "w", encoding="utf-8") as f:
        f.write(json.dumps(obj))


def load_from_file(file):
    with open(file, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == '__main__':
    str = '{"foo":"test", "bar":"123"}'
    write(read(str))
    pass
