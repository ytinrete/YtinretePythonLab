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


def iterate_folder(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            print('root:' + root + ' ' + 'name:' + name)


def list_sub_files(path):
    for file_name in os.listdir(path):
        full_path = os.path.join(path, file_name)
        stat_info = os.stat(full_path)
        print(full_path + ' size:' + convert_bytes(stat_info.st_size) + ' isFolder:' + str(os.path.isdir(full_path)))


def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def get_parent_folder(path):
    return os.path.abspath(os.path.join(path, os.pardir))


if __name__ == '__main__':
    # make_dir('test/test2/test3')
    # del_dir('test')

    # write_file('test/test2/test3/test.txt')
    # read_file('test/test2/test3/test.txt')
    # list_sub_files('.')
    print(get_parent_folder('./..'))

    pass
