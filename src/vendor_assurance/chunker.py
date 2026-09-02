"""Split large reports into manageable, overlapping text chunks."""

import re
from collections.abc import Iterator


def chunk_document(text: str, max_tokens: int = 500, overlap_tokens: int = 50) -> list[str]:
    """Return whitespace-tokenized chunks with a stable overlap.

    Chunking removes the single-upload bottleneck that affected the earlier low-code
    approach: callers can process each bounded section independently, then merge findings.
    The overlap preserves evidence that crosses a chunk boundary.
    """
    if max_tokens <= 0:
        raise ValueError("max_tokens must be positive")
    if overlap_tokens < 0 or overlap_tokens >= max_tokens:
        raise ValueError("overlap_tokens must be between zero and max_tokens - 1")

    token_matches = list(re.finditer(r"\S+", text))
    if not token_matches:
        return []

    step = max_tokens - overlap_tokens
    chunks = []
    for start in range(0, len(token_matches), step):
        end = min(start + max_tokens, len(token_matches))
        chunks.append(text[token_matches[start].start() : token_matches[end - 1].end()])
    return chunks


def iter_chunks(text: str, max_tokens: int = 500, overlap_tokens: int = 50) -> Iterator[str]:
    """Yield chunks for callers that do not want to retain a large report in memory."""
    yield from chunk_document(text, max_tokens, overlap_tokens)
