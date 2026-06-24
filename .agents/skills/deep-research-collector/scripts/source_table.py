#!/usr/bin/env python3
"""Render a Markdown evidence table from a JSON source list.

Input format:
[
  {
    "rank": 1,
    "source": "Official documentation title or URL",
    "type": "official docs",
    "date": "2026-01-01",
    "reliability": 5,
    "evidence": "Key fact or claim supported by the source",
    "use": "How this source informs the final answer"
  }
]

Usage:
  python .agents/skills/deep-research-collector/scripts/source_table.py sources.json
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

COLUMNS = [
    "Rank",
    "Source",
    "Type",
    "Date",
    "Reliability",
    "Key evidence",
    "Use in answer",
]


def cell(value: Any) -> str:
    """Escape a value for a Markdown table cell."""
    if value is None:
        return ""
    text = str(value).strip()
    return text.replace("|", "\\|").replace("\n", "<br>")


def load_sources(path: Path) -> list[dict[str, Any]]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"File not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path}: {exc}")

    if not isinstance(data, list):
        raise SystemExit("Input JSON must be a list of source objects.")

    for idx, item in enumerate(data, start=1):
        if not isinstance(item, dict):
            raise SystemExit(f"Source item {idx} is not an object.")

    return data


def render_table(sources: list[dict[str, Any]]) -> str:
    lines = []
    lines.append("| " + " | ".join(COLUMNS) + " |")
    lines.append("| " + " | ".join(["---"] * len(COLUMNS)) + " |")

    for idx, item in enumerate(sources, start=1):
        row = [
            item.get("rank", idx),
            item.get("source", ""),
            item.get("type", ""),
            item.get("date", ""),
            item.get("reliability", ""),
            item.get("evidence", ""),
            item.get("use", ""),
        ]
        lines.append("| " + " | ".join(cell(value) for value in row) + " |")

    return "\n".join(lines)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: source_table.py sources.json", file=sys.stderr)
        return 2

    sources = load_sources(Path(argv[1]))
    print(render_table(sources))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
