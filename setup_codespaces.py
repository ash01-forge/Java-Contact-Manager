#!/usr/bin/env python3
"""Restore the prepared Java project folders inside this Codespaces repository."""
import hashlib
from pathlib import Path, PurePosixPath
import zipfile

ROOT = Path(__file__).resolve().parent
EXPECTED_SHA256 = "5148e4d47ba7f220169eb1ddeae05531cdf08126f4c5a994d0332fa783e4d915"
PREFIX = "Java-Contact-Manager"


def main():
    if not (ROOT / ".git").exists():
        raise RuntimeError("Run this file from the repository root in GitHub Codespaces.")
    archives = sorted(ROOT.glob("Java-Contact-Manager-Codespaces*.zip"))
    archive = next((p for p in archives
                    if p.stat().st_size < 5_000_000
                    and hashlib.sha256(p.read_bytes()).hexdigest() == EXPECTED_SHA256), None)
    if archive is None:
        raise RuntimeError("Upload the matching Java-Contact-Manager-Codespaces.zip beside this setup file first.")
    files = []
    with zipfile.ZipFile(archive) as package:
        for item in package.infolist():
            if item.is_dir():
                continue
            path = PurePosixPath(item.filename)
            if path.is_absolute() or not path.parts or path.parts[0] != PREFIX:
                raise RuntimeError("Unexpected archive layout.")
            relative = PurePosixPath(*path.parts[1:])
            if not relative.parts or any(part in ("..", ".git") for part in relative.parts):
                raise RuntimeError("Unexpected archive path.")
            destination = ROOT.joinpath(*relative.parts)
            if not destination.resolve().is_relative_to(ROOT):
                raise RuntimeError("Archive path is outside the repository.")
            data = package.read(item)
            if destination.exists() and destination.read_bytes().replace(b"\r\n", b"\n") != data.replace(b"\r\n", b"\n"):
                raise RuntimeError("Existing file differs; nothing changed. Check: " + str(relative))
            files.append((destination, data))
    if len(files) != 21:
        raise RuntimeError("The package does not contain the expected 21 source/configuration files.")
    for destination, data in files:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
    print("DONE: all 21 project files are in their correct folders.")
    print("Next: save the changes with Source Control > Commit & Sync.")
    print("Then press Ctrl+Shift+P and run Codespaces: Rebuild Container.")
    print("After rebuilding, open PORTS > 6080 > Open in Browser; keep it Private.")
    print("No commit, push, or remote changes were performed by this setup file.")


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, zipfile.BadZipFile) as error:
        raise SystemExit("Setup stopped: " + str(error))
