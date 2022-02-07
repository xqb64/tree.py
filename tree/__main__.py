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


def traverse(path: pathlib.Path, depth=0) -> None:
    sorted_paths = traverse_paths(path)

    for idx, file in enumerate(sorted_paths, 1):
        is_last = idx == len(sorted_paths)
        prefix = '┃  ' * depth
        another_prefix = '┗━' if is_last else '┣━'
        if file.is_dir():
            print(f'{prefix}{another_prefix} {file.name}/')
            traverse(file, depth=depth+1)
        else:
            print(f'{prefix}{another_prefix} {file.name}')


def main() -> None:
    current = pathlib.Path('.')
    print('.')
    traverse(current)


if __name__ == '__main__':
    main()
