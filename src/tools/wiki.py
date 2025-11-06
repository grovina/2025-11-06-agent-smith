"""
Wikipedia lookup tool (no API key required).

We call the public REST Summary API to get a concise description and URL.
This gives students a small but exciting "live web" integration while staying
very simple.
"""

import re
import urllib.parse
from typing import Any

import requests  # type: ignore
from agents import function_tool


def _truncate(text: str, max_sentences: int) -> str:
    """Naively keep roughly the first N sentences to stay short."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return " ".join(parts[:max_sentences])


@function_tool
def wikipedia_lookup(topic: str) -> dict[str, Any]:
    """
    Look up a concise summary of a topic on Wikipedia.

    Args:
        topic: The topic to look up

    Returns:
        A dictionary with title and summary of the Wikipedia page
    """
    print(f'[Searching Wikipedia for "{topic}"...]')

    title_encoded = urllib.parse.quote(topic.strip().replace(" ", "_"))
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title_encoded}"

    response = requests.get(url, timeout=8)
    if response.status_code != 200:
        return {"error": f"status {response.status_code}"}

    data = response.json()
    page_title = data.get("title") or topic
    extract = data.get("extract") or ""

    return {"title": page_title, "summary": _truncate(extract, max_sentences=10)}
