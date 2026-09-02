import pytest

from src.vendor_assurance.chunker import chunk_document


def test_chunks_respect_boundary_and_overlap() -> None:
    tokens = [f"word-{number}" for number in range(25)]
    chunks = chunk_document(" ".join(tokens), max_tokens=10, overlap_tokens=3)

    assert all(len(chunk.split()) <= 10 for chunk in chunks)
    assert chunks[0].split()[-3:] == chunks[1].split()[:3]
    assert chunks[1].split()[-3:] == chunks[2].split()[:3]
    assert chunks[-1].split()[-1] == "word-24"


def test_invalid_overlap_is_rejected() -> None:
    with pytest.raises(ValueError):
        chunk_document("some text", max_tokens=10, overlap_tokens=10)
