from pathlib import  Path

import shutil

class FileMoveError(Exception):
    pass

def rename_file(destination_path:Path):

    parent = destination_path.parent
    stem = destination_path.stem
    suffix = destination_path.suffix
    counter = 1

    while destination_path.exists():
        destination_path = parent / f"{stem}_{counter}{suffix}"
        counter += 1
    return destination_path


def file_mover(base_path:Path,file_path:Path,destination:str) -> Path:

    destination_dir = base_path / destination

    destination_dir.mkdir(parents=True, exist_ok=True)

    destination_path = destination_dir / file_path.name

    if destination_path.exists():
        destination_path = rename_file(destination_path)

    try:
        shutil.move(file_path, destination_path)

    except OSError:
        raise FileMoveError(f"failed to move file {file_path} to {destination_path}")

    return destination_path






