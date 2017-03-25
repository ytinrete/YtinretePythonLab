import shutil
import os


def copy_folder(from_path, to_path):
    shutil.copytree(from_path, to_path)


def make_dir(path):
    if not os.path.isdir(path):
        try:
            os.makedirs(path)
            return True
        except FileExistsError or OSError as e:
            print(e)
    else:
        print("already exist!")
        return False


def del_dir(path):
    shutil.rmtree(path)


def read_file(path):
    if os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as f:
            print(f.read())


def write_file(path):
    with open(path, 'w', encoding='utf-8') as f:
        f.write('233')


if __name__ == '__main__':
    # make_dir('test/test2/test3')
    # del_dir('test')

    # write_file('test/test2/test3/test.txt')
    # read_file('test/test2/test3/test.txt')
    pass
