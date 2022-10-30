from os import listdir
from os import rename
from os.path import isfile, join
import re


def rename_files(path):
    files = [f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.mp3')]
    files.sort()
    print(files)

    for idx, f in enumerate(files):
        m = re.search('^\\d+-', f)

        new_name = f'{str(idx + 1).zfill(2)} - {f[m.end():]}'
        print(new_name)

        rename(join(path, f), join(path, new_name))


def starts_with_number(filename):
    return '^./'


if __name__ == '__main__':
    rename_files('/home/seb/Musique/ab_divers/compiles/2022, mum')
