#!/usr/bin/env python3
"""Verify PDF content parity against the manuscript (word-level subsequence check).

Method:
1. Extract all text from the PDF page by page; join with spaces; normalize whitespace.
2. Normalize the manuscript: strip markdown syntax (#, ##, >, -, *, **, TOC
   brackets/anchors), keep punctuation.
3. Tokenize both into words (lowercase). Use difflib.SequenceMatcher to find
   manuscript token runs that cannot be matched in the PDF (allowing front-matter
   insertions). Report runs of >= 3 consecutive manuscript words.
4. Report word counts for both.
"""
import re
import sys
from difflib import SequenceMatcher

from pypdf import PdfReader

MD_PATH = "manuscript/Mystery_of_the_Trinity.md"
PDF_PATH = "manuscript/Mystery_of_the_Trinity.pdf"


def extract_pdf_text(path: str) -> str:
    reader = PdfReader(path)
    pages = []
    for p in reader.pages:
        pages.append(p.extract_text() or "")
    return " ".join(pages)


def normalize_md(text: str) -> str:
    out_lines = []
    for line in text.splitlines():
        line = line.rstrip()
        # TOC list entries: "- [Chapter 1 — Icons of the Trinity](#chapter-1-...)"
        if line.startswith("- [") and "](#" in line:
            line = line[3:]  # drop "- ["
            line = re.sub(r"\]\(#.*?\)$", "", line)
        else:
            # strip blockquote markers / list bullets / heading hashes
            line = re.sub(r"^\s{0,3}(>|\d+\.|-|\*)\s?", "", line)
            line = re.sub(r"^\s{0,3}#{1,6}\s?", "", line)
            # inline markdown: images/links (keep text), bold/italic markers, code ticks
            line = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line)
            line = line.replace("**", "").replace("__", "").replace("`", "")
            line = line.replace("*", "")
        out_lines.append(line)
    text = "\n".join(out_lines)
    return text


def norm_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def tokenize(text: str):
    return re.findall(r"[A-Za-z0-9'’\-]+|[^\sA-Za-z0-9'’\-]+", norm_ws(text).lower())


def main() -> int:
    pdf_raw = norm_ws(extract_pdf_text(PDF_PATH))
    md_norm = norm_ws(normalize_md(open(MD_PATH, encoding="utf-8").read()))

    pdf_toks = tokenize(pdf_raw)
    md_toks = tokenize(md_norm)
    pdf_words = [t for t in pdf_toks if re.match(r"[a-z0-9'’\-]", t)]
    md_words = [t for t in md_toks if re.match(r"[a-z0-9'’\-]", t)]

    print(f"PDF pages: {len(PdfReader(PDF_PATH).pages)}")
    print(f"PDF total tokens: {len(pdf_toks)}, words: {len(pdf_words)}")
    print(f"MD total tokens: {len(md_toks)}, words: {len(md_words)}")
    print(f"Word diff (PDF - MD): {len(pdf_words) - len(md_words)}")
    print()

    sm = SequenceMatcher(None, md_words, pdf_words, autojunk=False)
    opcodes = sm.get_opcodes()
    missing_runs = []
    total_matched = 0
    for tag, i1, i2, j1, j2 in opcodes:
        if tag == "equal":
            total_matched += i2 - i1
        elif tag == "delete":  # manuscript words not found in PDF
            run = " ".join(md_words[i1:i2])
            if i2 - i1 >= 3:
                missing_runs.append((i1, i2 - i1, run))
    print(f"Matched manuscript words: {total_matched} / {len(md_words)}")
    print(f"Missing manuscript words: {len(md_words) - total_matched}")
    print(f"Missing runs (>=3 consecutive words): {len(missing_runs)}")
    for i1, ln, run in missing_runs:
        # print a little context
        ctx = " ".join(md_words[max(0, i1 - 6):i1])
        print(f"\n  @ word index {i1} ({ln} words):")
        print(f"    ...{ctx}")
        print(f"    MISSING: {run[:200]}")

    ratio = sm.ratio()
    print(f"\nSequenceMatcher ratio: {ratio:.6f}")
    return 0 if not missing_runs else 1


if __name__ == "__main__":
    sys.exit(main())
