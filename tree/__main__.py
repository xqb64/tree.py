import argparse
import pathlib
import typing as t


def traverse(
    path: pathlib.Path,
    exclude_hidden_files: bool,
    is_parent_last: bool,
    depth: int = 0
) -> None:
    paths = list(path.iterdir())
    for idx, p in enumerate(paths, 1):
        if exclude_hidden_files and p.name.startswith('.'):
            continue

        is_last = idx == len(paths)

        prefix = "┗━" if is_last else "┣━" 
        parent_prefix =  ("┃ " * (depth-1) + "  ") if is_parent_last else ("┃ " * depth)

        if p.is_symlink():
            print(f"{parent_prefix}{prefix}", p.name, "->", p.resolve())
            continue
        if p.is_dir():
            print(f"{parent_prefix}{prefix}", p.name)
            traverse(p, exclude_hidden_files=exclude_hidden_files, is_parent_last=is_last, depth=depth+1)
        else:
            print(f"{parent_prefix}{prefix}", p.name)


def main(args: argparse.Namespace) -> None:
    current = pathlib.Path(args.path)
    print(args.path)
    traverse(current, exclude_hidden_files=args.exclude_hidden_files, is_parent_last=False)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--exclude-hidden-files', action='store_true')
    parser.add_argument('path')
    args = parser.parse_args()
    main(args)
