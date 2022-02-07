import pathlib

def build_prefix(depth: int) -> str:
    return ('  ' + '┃') * depth

def traverse(path: pathlib.Path, depth=0) -> None:
    dirs = []
    files = []

    for file in path.iterdir():
        if file.is_dir():
            dirs.append(file)
        else:
            files.append(file)

    sorted_paths = dirs + files

    for idx, file in enumerate(sorted_paths, 1):
        is_last = idx == len(sorted_paths)
        prefix = build_prefix(depth)
        filename_prefix = '┗━' if is_last else '┣━'
        if file.is_dir():
            print(f'{prefix}  {filename_prefix} {file.name}/')
            traverse(file, depth=depth+1)
        else:
            print(f'{prefix}  {filename_prefix} {file.name}')

def main():
    current = pathlib.Path('.')
    print(f'  {current.resolve().name}/')
    traverse(current)

if __name__ == '__main__':
    main()