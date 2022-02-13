import argparse
import pathlib
import typing as t

def sieve(path: pathlib.Path) -> t.List[pathlib.Path]:
    directories = []
    files = []
    for file in path.iterdir():
        if file.is_dir():
            directories.append(file)
        else:
            files.append(file)
    return directories + files


def traverse(path: pathlib.Path, exclude_hidden_files: bool, depth: int = 0) -> None:
    paths = sieve(path)
    for idx, p in enumerate(paths, 1):
        grandparents = sieve(p.parent.parent) + [path]

        is_last = idx == len(paths)
        is_parent_last = grandparents.index(p.parent) + 1 == len(grandparents) - 1

        prefix = "┗━" if is_last else "┣━" 
        parent_prefix =  ("┃ " * (depth-1) + "  ") if is_parent_last else ("┃ " * depth)

        if p.is_symlink():
            print(f"{parent_prefix}{prefix}", p.name, "->", p.resolve())
            continue
        if p.is_dir():
            print(f"{parent_prefix}{prefix}", p.name)
            traverse(p, exclude_hidden_files=exclude_hidden_files, depth=depth+1)
        else:
            print(f"{parent_prefix}{prefix}", p.name)


def main(args: argparse.Namespace) -> None:
    current = pathlib.Path('.')
    print('.')
    traverse(current, exclude_hidden_files=args.exclude_hidden_files)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--exclude-hidden-files')
    args = parser.parse_args()
    main(args)
