import pathlib

from modules import *


def main():
    try:
        _url = str(input('URL: '))
        new = check_url(_url)
        answer = get_data(new)
        write_to_excel(answer)
    except Exception as e:
        print(e)
    finally:
        print(f'file is created here: {pathlib.Path.cwd()}')


if __name__ == '__main__':
    main()