from pathlib import Path


def is_inside_target_folder(file_path : Path ,target_folder: list[Path]) -> bool:
    for path in target_folder:
        try:
            file_path.relative_to(path)
            return True
        except ValueError:
            continue
    return False

def scan_folder(path : Path , target_folder):

    if not path.exists():
        raise FileNotFoundError()

    for path in Path(path).rglob("*"):
        if path.is_file() and is_inside_target_folder(path,target_folder):
           yield path






