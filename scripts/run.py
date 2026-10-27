#!/usr/bin/env python3
"""Build and launch the original Java Swing app in the Codespaces desktop."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"
CLASSES = BUILD / "classes"
MAIN_CLASS = "com.mycompany.assignmentfinal2.Start"


def tool(name):
    return os.environ.get(name.upper() + "_BIN", name)


def build():
    classes = CLASSES
    classes.mkdir(parents=True, exist_ok=True)
    sources = sorted((ROOT / "src" / "main" / "java").rglob("*.java"))
    if not sources:
        raise RuntimeError("No Java source files found.")
    subprocess.run([tool("javac"), "--release", "17", "-encoding", "UTF-8",
                    "-d", str(classes), *map(str, sources)], cwd=ROOT, check=True)
    print("Build complete: build/classes", flush=True)


def desktop_ready():
    if os.name != "nt" and not os.environ.get("DISPLAY"):
        raise RuntimeError("No graphical display. Rebuild the Codespaces container with the included configuration.")
    if shutil.which("xdpyinfo"):
        for _ in range(30):
            ready = subprocess.run(["xdpyinfo", "-display", os.environ.get("DISPLAY", ":1")],
                                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if ready.returncode == 0:
                return
            time.sleep(1)
        raise RuntimeError("Desktop service is not ready. Rebuild the container, then run the Open app task again.")


def already_running():
    # A Linux PID can be recycled, so check the actual Java command as well.
    try:
        pid = int((BUILD / "app.pid").read_text().strip())
        if pid <= 0:
            return False
        command = Path("/proc") / str(pid) / "cmdline"
        args = command.read_bytes().split(b"\0")
        return os.fsencode(str(CLASSES)) in args and os.fsencode(MAIN_CLASS) in args
    except (OSError, ValueError):
        return False


def launch(background):
    desktop_ready()
    if already_running():
        print("App is already running. Open PORTS > 6080 > Open in Browser.")
        return
    command = [tool("java"), "-cp", str(CLASSES), MAIN_CLASS]
    if not background:
        subprocess.run(command, cwd=ROOT, check=True)
        return
    log_path = BUILD / "app.log"
    with log_path.open("ab") as log:
        app = subprocess.Popen(command, cwd=ROOT, stdin=subprocess.DEVNULL,
                               stdout=log, stderr=subprocess.STDOUT,
                               start_new_session=True)
    (BUILD / "app.pid").write_text(str(app.pid) + "\n", encoding="utf-8")
    time.sleep(1)
    if app.poll() is not None:
        details = log_path.read_text(encoding="utf-8", errors="replace")[-4000:]
        raise RuntimeError("App exited during startup. See build/app.log:\n" + details)
    print("Java Contact Manager started. Open PORTS > 6080 > Open in Browser.")
    print("Connect to the desktop with its configured password (default: vscode).")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--build-only", action="store_true")
    modes.add_argument("--background", action="store_true")
    modes.add_argument("--foreground", action="store_true")
    args = parser.parse_args()
    build()
    if not args.build_only:
        launch(args.background)


if __name__ == "__main__":
    try:
        main()
    except (OSError, RuntimeError, subprocess.CalledProcessError) as error:
        print("Error: " + str(error), file=sys.stderr)
        sys.exit(1)
