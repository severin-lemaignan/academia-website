#!/usr/bin/env python3
"""
Add a talk to the website.

Usage:
    python3 add_talk.py \
        --pdf static/talks/2026-hri-responsible-humanoids.pdf \
        --title "Responsible Humanoids" \
        --date 2026-03-04 \
        --venue "HRI 2026, Melbourne" \
        --summary "Keynote on responsible design of humanoid robots" \
        --page 1 \
        --papers lemaignan2024probabilistic ferrini2025percepts

This will:
1. Extract the specified page from the PDF as a JPEG poster thumbnail
   → static/talks/posters/<pdf-basename>.jpg
2. Append the talk entry to static/talks.json
"""

import argparse
import json
import os
import subprocess
import sys

TALKS_JSON = os.path.join(os.path.dirname(__file__), "static", "talks.json")
POSTERS_DIR = os.path.join(os.path.dirname(__file__), "static", "talks", "posters")


def extract_poster(pdf_path: str, page: int, output_path: str) -> None:
    """Extract a single page from a PDF as a JPEG image using pdftoppm."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # pdftoppm outputs <prefix>-<pagenumber>.jpg, so we use a temp prefix
    # and then rename to desired output path
    prefix = output_path.replace(".jpg", "")
    subprocess.run(
        [
            "pdftoppm",
            "-jpeg",
            "-r", "150",          # 150 DPI — good balance of quality/size
            "-f", str(page),
            "-l", str(page),
            "-singlefile",
            pdf_path,
            prefix,
        ],
        check=True,
    )

    generated = prefix + ".jpg"
    if generated != output_path:
        os.rename(generated, output_path)

    print(f"  ✓ Poster saved to {output_path}")


def add_talk(
    pdf: str,
    title: str,
    date: str,
    venue: str,
    summary: str,
    page: int,
    papers: list[str] | None = None,
) -> None:
    # Resolve paths relative to the project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_abs = os.path.join(script_dir, pdf) if not os.path.isabs(pdf) else pdf

    if not os.path.exists(pdf_abs):
        print(f"Error: PDF not found: {pdf_abs}", file=sys.stderr)
        sys.exit(1)

    # Derive the poster filename from the PDF basename
    basename = os.path.splitext(os.path.basename(pdf))[0]
    poster_filename = f"{basename}.jpg"
    poster_abs = os.path.join(POSTERS_DIR, poster_filename)

    # The paths stored in JSON are relative to static/ (for use as URL paths)
    pdf_rel = pdf.replace("static/", "", 1) if pdf.startswith("static/") else pdf
    poster_rel = f"talks/posters/{poster_filename}"

    # 1. Extract poster
    print(f"Extracting page {page} from {pdf}...")
    extract_poster(pdf_abs, page, poster_abs)

    # 2. Read existing talks
    if os.path.exists(TALKS_JSON):
        with open(TALKS_JSON, "r") as f:
            talks = json.load(f)
    else:
        talks = []

    # Check for duplicates (by PDF path)
    if any(t["pdf"] == pdf_rel for t in talks):
        print(f"  ⚠ Talk with PDF '{pdf_rel}' already exists in talks.json — skipping.")
        return

    # 3. Add new entry
    entry = {
        "title": title,
        "date": date,
        "venue": venue,
        "summary": summary,
        "pdf": pdf_rel,
        "poster": poster_rel,
    }
    if papers:
        entry["papers"] = papers
    talks.append(entry)

    # Sort by date descending
    talks.sort(key=lambda t: t["date"], reverse=True)

    # 4. Write back
    with open(TALKS_JSON, "w") as f:
        json.dump(talks, f, indent=2, ensure_ascii=False)

    print(f"  ✓ Added '{title}' to {TALKS_JSON}")
    print(f"  Total talks: {len(talks)}")


def main():
    parser = argparse.ArgumentParser(
        description="Add a talk to the website",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--pdf", required=True, help="Path to the PDF (relative to project root)")
    parser.add_argument("--title", required=True, help="Talk title")
    parser.add_argument("--date", required=True, help="Date of the talk (YYYY-MM-DD)")
    parser.add_argument("--venue", required=True, help="Venue or context (e.g. 'HRI 2026, Melbourne')")
    parser.add_argument("--summary", required=True, help="One-line summary of the talk")
    parser.add_argument("--page", type=int, default=1, help="PDF page to use as poster (default: 1)")
    parser.add_argument("--papers", nargs="*", default=None, help="Publication IDs for related papers (e.g. lemaignan2024probabilistic)")

    args = parser.parse_args()
    add_talk(args.pdf, args.title, args.date, args.venue, args.summary, args.page, args.papers)


if __name__ == "__main__":
    main()
