"""The World in One Day -- 26 November 2026.

A one-day world news front page for make.fun's news-image-20261126
bounty ("Sum up 26 November's world news in one image").

The page itself was drawn ahead of time and is shipped in this repo as
entry.png: a 1024x1024 newspaper front page with the masthead
"THE WORLD IN ONE DAY", dated Thursday, 26 November 2026. Its lead story
is the Houthis' claimed strike on Saudi Arabia's Ras Tanura refinery,
with five further panels -- the Cairo tanker fire, the Mississippi plane
crash, the Hera images of asteroid Dimorphos, Pakistan's first astronaut
reaching Tiangong, and the freed Cartagena hostages -- plus an "Also
today" footer strip of eight smaller headlines.

The stories were researched from real reporting of the day (Reuters, AP,
AFP, ESA, Nature): the top stories were first reported on 25 November
UTC, which is 26 November in Asia, and they lead the 26 November
editions -- the day this competition sums up.

This program does the one thing the run needs: it copies the shipped
entry.png into the output directory the harness points at with the
MAKEFUN_OUTPUT_DIR environment variable (falling back to ./output).
It uses only the Python standard library, because the grading sandbox
runs Python 3.13 with nothing else installed.
"""

import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"shipped image not found: {source}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    # Sanity check: the copy must still start with the PNG signature.
    if target.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"output is not a PNG file: {target}")
    print(f"copied {source} -> {target} ({target.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
