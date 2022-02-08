import argparse
import pathlib
import typing as t


def traverse_paths(path: pathlib.Path) -> t.List[pathlib.Path]:
    dirs = []
    files = []

    for file in path.iterdir():
        if file.is_dir():
            dirs.append(file)
        else:
            files.append(file)

    return dirs + files


def traverse(path: pathlib.Path, exclude_hidden_files: bool, depth=0) -> None:
    sorted_paths = traverse_paths(path)

    for idx, file in enumerate(sorted_paths, 1):
        if exclude_hidden_files and file.name.startswith('.'):
            continue
        is_last = idx == len(sorted_paths)
        prefix = '┃  ' * depth
        another_prefix = '┗━' if is_last else '┣━'
        if file.is_dir():
            print(f'{prefix}{another_prefix} {file.name}/')
            traverse(file, exclude_hidden_files=exclude_hidden_files, depth=depth+1)
        else:
            print(f'{prefix}{another_prefix} {file.name}')


def main(args: argparse.Namespace) -> None:
    exclude_hidden_files = args.exclude_hidden_files 

    current = pathlib.Path('.')
    print('.')
    traverse(current, exclude_hidden_files=exclude_hidden_files)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--exclude-hidden-files')
    args = parser.parse_args()
    main(args)
