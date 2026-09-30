#!/usr/bin/env python3
"""Render probe results from TSV on stdin as a terminal table.

Each row is six tab-separated fields: case, request, result, status, bytes, evidence.
"""

from __future__ import annotations

import argparse
import sys

HEADERS = ("Case", "Request", "Result", "Status", "Bytes", "Evidence")
RIGHT_ALIGNED = {3, 4}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--footer",
        action="append",
        default=[],
        help="Line printed under the table. Repeat for more than one line.",
    )
    return parser.parse_args()


def read_rows() -> list[tuple[str, str, str, str, str, str]]:
    rows: list[tuple[str, str, str, str, str, str]] = []
    for line_number, raw in enumerate(sys.stdin, start=1):
        line = raw.rstrip("\n")
        if line.strip() == "":
            continue
        parts = line.split("\t")
        if len(parts) != 6:
            raise SystemExit(
                f"line {line_number}: expected 6 tab-separated fields, got {len(parts)}"
            )
        case, request, result, status, nbytes, evidence = (part.strip() for part in parts)
        if case == "" or request == "" or evidence == "":
            raise SystemExit(f"line {line_number}: case, request, and evidence are required")
        if result not in {"pass", "fail"}:
            raise SystemExit(f"line {line_number}: result must be pass or fail")
        if status != "-" and not status.isdigit():
            raise SystemExit(f"line {line_number}: status must be an HTTP code or -")
        if nbytes != "-" and not nbytes.isdigit():
            raise SystemExit(f"line {line_number}: bytes must be a number or -")
        rows.append((case, request, result, status, nbytes, evidence))
    if not rows:
        raise SystemExit("no rows on stdin")
    return rows


def cell(text: str, width: int, index: int) -> str:
    if index in RIGHT_ALIGNED:
        return text.rjust(width)
    return text.ljust(width)


def render_table(rows: list[tuple[str, ...]]) -> str:
    widths = [len(header) for header in HEADERS]
    for row in rows:
        for index, value in enumerate(row):
            widths[index] = max(widths[index], len(value))

    def line(left: str, mid: str, right: str) -> str:
        segments = ["─" * (width + 2) for width in widths]
        return left + mid.join(segments) + right

    def render(row: tuple[str, ...]) -> str:
        padded = [f" {cell(value, widths[index], index)} " for index, value in enumerate(row)]
        return "│" + "│".join(padded) + "│"

    body = [render(row) for row in rows]
    return "\n".join(
        [
            line("┌", "┬", "┐"),
            render(HEADERS),
            line("├", "┼", "┤"),
            *body,
            line("└", "┴", "┘"),
        ]
    )


def main() -> None:
    args = parse_args()
    rows = read_rows()
    print(render_table(rows))
    if args.footer:
        print()
        for footer in args.footer:
            print(footer)


if __name__ == "__main__":
    main()
