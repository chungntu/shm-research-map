"""Build the public index.html from the local research map.

The local file keeps private details (manuscript IDs, handling editor,
co-authors, drive paths); this script strips them before publishing.
Usage: python build_public.py
"""
import re
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "ban_do_nghien_cuu_SHM_2026-09-04.html"
OUT = HERE / "index.html"

s = SRC.read_text(encoding="utf-8")

# Private notes in the journal column
s = re.sub(r"[ \t]*<small>(MS ID|HE|Co-author)s?:.*?</small>\n", "", s)

# Drive-path column (header + cells)
s = re.sub(r"[ \t]*<th>Project Folder on Drive</th>\n", "", s)
s = re.sub(r'[ \t]*<td class="col-path">.*?</td>\n', "", s)
s = s.replace(", submitted / target journal, manuscript ID, and project folder location",
              " and submitted / target journal")

# Local HTML comments (paper numbers, notes)
s = re.sub(r"[ \t]*<!--.*?-->\n", "", s, flags=re.S)

leaks = [p for p in ("MS ID", "HE:", "Co-author", "E:\\", "e:\\", "col-path\">")
         if p in s]
if leaks:
    raise SystemExit(f"Private details still present: {leaks}")

OUT.write_text(s, encoding="utf-8")
print(f"Wrote {OUT.name}")
