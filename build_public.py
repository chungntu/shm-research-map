"""Build the public index.html from the local research map.

The full map is published as is (the author chose not to hide any details).
Usage: python build_public.py
"""
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "ban_do_nghien_cuu_SHM_2026-09-04.html"
OUT = HERE / "index.html"

if SRC.exists():
    OUT.write_text(SRC.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Updated {OUT.name} from {SRC.name}")
else:
    print(f"{OUT.name} is the direct source of truth ({SRC.name} not present). No overwrite performed.")

