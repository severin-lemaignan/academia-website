#!/usr/bin/env python3
"""
Add a publication to the website using its DOI.

Usage:
    python3 add_paper.py 10.1109/mra.2025.3620148
    python3 add_paper.py 10.1109/mra.2025.3620148 --pdf publis/myfile.pdf --type journal --keywords "Ethics" "Robotics"

Fetches metadata from doi.org (Crossref), generates a BibTeX entry, and
appends the publication to static/publications.json.
"""

import argparse
import json
import os
import re
import sys
import unicodedata
import urllib.request
import urllib.error

PUBLICATIONS_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "publications.json")


def fetch_crossref_metadata(doi: str) -> dict:
    """Fetch structured metadata from Crossref via content negotiation."""
    url = f"https://api.crossref.org/works/{doi}"
    req = urllib.request.Request(url, headers={"User-Agent": "add_paper.py (academic website builder)"})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["message"]
    except urllib.error.HTTPError as e:
        print(f"Error fetching metadata for DOI {doi}: HTTP {e.code}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error fetching metadata for DOI {doi}: {e}", file=sys.stderr)
        sys.exit(1)


def fetch_bibtex(doi: str) -> str:
    """Fetch BibTeX entry via DOI content negotiation."""
    url = f"https://doi.org/{doi}"
    req = urllib.request.Request(url, headers={
        "Accept": "application/x-bibtex",
        "User-Agent": "add_paper.py (academic website builder)",
    })
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8").strip()
    except Exception as e:
        print(f"  ⚠ Could not fetch BibTeX: {e}", file=sys.stderr)
        return ""


def strip_accents(s: str) -> str:
    """Remove accents from a string for ID generation."""
    return "".join(
        c for c in unicodedata.normalize("NFD", s)
        if unicodedata.category(c) != "Mn"
    )


def make_id(authors: list[dict], year: int, title: str) -> str:
    """Generate a publication ID like 'lemaignan2025robotics'."""
    if authors:
        # Use first author's family name
        family = authors[0].get("family", "unknown")
        family = strip_accents(family).lower()
        family = re.sub(r"[^a-z]", "", family)
    else:
        family = "unknown"

    # First significant word from title (skip short words)
    skip = {"a", "an", "the", "of", "for", "in", "on", "to", "and", "with", "from", "by", "at", "is", "are", "was"}
    words = re.findall(r"[a-z]+", title.lower())
    keyword = "paper"
    for w in words:
        if w not in skip and len(w) > 2:
            keyword = w
            break

    return f"{family}{year}{keyword}"


def format_author(author: dict) -> str:
    """Format a Crossref author dict to 'LastName, Initials.' format."""
    family = author.get("family", "")
    given = author.get("given", "")
    if given:
        # Convert given names to initials
        initials = ". ".join(part[0] for part in given.split() if part) + "."
        return f"{family}, {initials}"
    return family


def detect_type(crossref: dict) -> str:
    """Map Crossref type to our publication type."""
    cr_type = crossref.get("type", "")
    type_map = {
        "journal-article": "journal",
        "proceedings-article": "conference",
        "book-chapter": "chapter",
        "book": "chapter",
        "dataset": "dataset",
        "posted-content": "conference",
        "report": "conference",
    }
    return type_map.get(cr_type, "conference")


def extract_venue(crossref: dict) -> str:
    """Extract venue name from Crossref metadata."""
    # Try container-title first (journal/conference name)
    containers = crossref.get("container-title", [])
    if containers:
        return containers[0]
    # Fall back to event name
    event = crossref.get("event", {})
    if event and event.get("name"):
        return event["name"]
    # Fall back to publisher
    return crossref.get("publisher", "")


def extract_year(crossref: dict) -> int:
    """Extract publication year from Crossref metadata."""
    # Try published-print first, then published-online, then created
    for field in ["published-print", "published-online", "published", "created"]:
        if field in crossref and "date-parts" in crossref[field]:
            parts = crossref[field]["date-parts"][0]
            if parts and parts[0]:
                return parts[0]
    return 0


def add_paper(doi: str, **overrides) -> None:
    print(f"Fetching metadata for DOI: {doi}...")

    crossref = fetch_crossref_metadata(doi)

    title = crossref.get("title", ["Untitled"])[0]
    authors_raw = crossref.get("author", [])
    year = extract_year(crossref)
    venue = extract_venue(crossref)
    pub_type = detect_type(crossref)
    pub_id = make_id(authors_raw, year, title)

    authors = [format_author(a) for a in authors_raw]

    print(f"  Title: {title}")
    print(f"  Authors: {', '.join(authors[:3])}{'...' if len(authors) > 3 else ''}")
    print(f"  Year: {year}, Venue: {venue}")
    print(f"  Type: {pub_type}, ID: {pub_id}")

    # Fetch BibTeX
    print("  Fetching BibTeX...")
    bibtex = fetch_bibtex(doi)

    # Replace the BibTeX key with our generated ID
    if bibtex:
        bibtex = re.sub(r"(@\w+\{)[^,]+,", rf"\1{pub_id},", bibtex, count=1)
        # Escape newlines for JSON storage (matching existing format)
        bibtex = bibtex.replace("\n", "\\n")

    # Build publication entry
    entry = {
        "id": pub_id,
        "type": pub_type,
        "title": title,
        "authors": authors,
        "venue": venue,
        "year": year,
        "doi": doi,
    }

    if bibtex:
        entry["bibtex"] = bibtex

    # Apply overrides
    if overrides.get("pdf"):
        entry["pdf"] = overrides["pdf"]
    if overrides.get("type"):
        entry["type"] = overrides["type"]
    if overrides.get("keywords"):
        entry["keywords"] = overrides["keywords"]
    if overrides.get("url"):
        entry["url"] = overrides["url"]
    if overrides.get("note"):
        entry["note"] = overrides["note"]
    if overrides.get("id"):
        entry["id"] = overrides["id"]
        pub_id = overrides["id"]
        # Also update bibtex key if we have bibtex
        if bibtex:
            entry["bibtex"] = re.sub(r"(@\w+\{)[^,]+,", rf"\1{pub_id},", bibtex.replace("\\n", "\n"), count=1).replace("\n", "\\n")

    # Read existing publications
    if os.path.exists(PUBLICATIONS_JSON):
        with open(PUBLICATIONS_JSON, "r") as f:
            publications = json.load(f)
    else:
        publications = []

    # Check for duplicates
    if any(p.get("doi") == doi for p in publications):
        print(f"  ⚠ Publication with DOI '{doi}' already exists — skipping.")
        return

    if any(p["id"] == pub_id for p in publications):
        print(f"  ⚠ Publication with ID '{pub_id}' already exists — skipping.")
        print(f"    Use --id to specify a different ID.")
        return

    # Prepend the new entry (don't sort, as the presentation relies on the existing order)
    publications.insert(0, entry)

    # Write back
    with open(PUBLICATIONS_JSON, "w") as f:
        json.dump(publications, f, indent=4, ensure_ascii=False)

    print(f"  ✓ Added '{title}' as '{pub_id}' to {PUBLICATIONS_JSON}")
    print(f"  Total publications: {len(publications)}")


def main():
    parser = argparse.ArgumentParser(
        description="Add a publication to the website using its DOI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("doi", help="DOI of the publication (e.g. 10.1109/mra.2025.3620148)")
    parser.add_argument("--pdf", help="Path to the PDF relative to static/ (e.g. publis/myfile.pdf)")
    parser.add_argument("--type", choices=["journal", "conference", "chapter", "dataset", "patent", "poster", "video", "abstract - conference"],
                        help="Override publication type")
    parser.add_argument("--keywords", nargs="*", help="Keywords (e.g. 'Social Robotics' 'HRI')")
    parser.add_argument("--url", help="External URL for the publication")
    parser.add_argument("--note", help="Note (e.g. 'under review')")
    parser.add_argument("--id", help="Override the auto-generated publication ID")

    args = parser.parse_args()
    add_paper(
        args.doi,
        pdf=args.pdf,
        type=args.type,
        keywords=args.keywords,
        url=args.url,
        note=args.note,
        id=args.id,
    )


if __name__ == "__main__":
    main()
