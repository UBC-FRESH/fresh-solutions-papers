#!/usr/bin/env python3
"""Count the SoftwareX manuscript words.

Counts the abstract, running text, captions, and footnotes. Excludes the
title/author block, the code-metadata table, the reference list, equations,
and the contents of data tables. This is the convention used in README.md.
"""

from __future__ import annotations

import re
import sys


def count_words(text: str) -> int:
    """Return the number of word tokens containing a letter or digit."""
    text = re.sub(r"%.*", "", text)
    text = re.sub(r"\\begin\{(align|equation)\}.*?\\end\{\1\}", "", text, flags=re.S)
    text = re.sub(r"\\begin\{tabular\}.*?\\end\{tabular\}", "", text, flags=re.S)
    text = re.sub(r"\$[^$\n]*\$", " X ", text)
    text = re.sub(r"\\cite[pt]?\{[^}]*\}", " ", text)
    text = re.sub(r"\\ref\{[^}]*\}", " 1 ", text)
    text = re.sub(r"\\url\{([^}]*)\}", r" \1 ", text)
    text = re.sub(r"\\[a-zA-Z]+\*?(\[[^\]]*\])?", " ", text)
    text = text.replace("{", " ").replace("}", " ").replace("~", " ")
    text = re.sub(r"--", " ", text)
    return len([w for w in text.split() if re.search(r"[A-Za-z0-9]", w)])


def main() -> int:
    """Print the counted word total for the SoftwareX draft."""
    path = sys.argv[1] if len(sys.argv) > 1 else "paper1-softwarex.tex"
    source = open(path, encoding="utf-8").read()
    main_text = source[source.index(r"\begin{abstract}") : source.index(r"\section*{Code metadata}")]
    availability = source[
        source.index(r"\section*{Data and code availability}") : source.index(r"\bibliographystyle")
    ]
    main_words = count_words(main_text)
    availability_words = count_words(availability)
    print(f"main text + captions: {main_words}")
    print(f"data availability:    {availability_words}")
    print(f"total counted:        {main_words + availability_words}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
