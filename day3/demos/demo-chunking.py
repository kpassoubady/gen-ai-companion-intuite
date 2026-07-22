"""
Demo - Chunking Strategies for RAG
Day 3 - Session 3

Goal: Show how fixed-size and overlapping chunking split a document differently,
and why overlap avoids cutting an idea in half at a boundary.

We take one sample document and chunk it three ways: fixed-size with no overlap,
fixed-size with overlap, and paragraph-based. For each we print the chunk count
and a preview so students see the tradeoffs. Overlap repeats a little text across
neighbors so a sentence split by a boundary still appears whole in one chunk.

No API key, no downloads. Pure Python.

Run: python3 day3/demos/demo-chunking.py
"""

DOCUMENT = """QuickBooks lets small businesses track income and expenses in one place.
You connect a bank account and transactions import automatically each day.
Each transaction can be categorized into a chart of accounts for reporting.

Invoices are created from the Sales menu and can be emailed to customers.
You can set payment terms, add line items, and apply sales tax per region.
Overdue invoices trigger automatic reminders if you enable them in settings.

Reports summarize profit and loss, balance sheet, and cash flow over a period.
You can filter any report by date range, customer, or class before exporting.
Exported reports save as PDF or CSV for sharing with an accountant."""


def chunk_fixed(text, size, overlap=0):
    """Split text into word windows of `size` with `overlap` words repeated."""
    words = text.split()
    step = size - overlap
    chunks = []
    for start in range(0, len(words), step):
        chunk = words[start:start + size]
        if chunk:
            chunks.append(" ".join(chunk))
        if start + size >= len(words):
            break
    return chunks


def chunk_paragraphs(text):
    """Split on blank lines so each chunk holds one paragraph."""
    return [p.strip().replace("\n", " ") for p in text.split("\n\n") if p.strip()]


def preview(chunk, width=70):
    """First `width` characters of a chunk, for compact printing."""
    flat = " ".join(chunk.split())
    return flat if len(flat) <= width else flat[:width] + "..."


def show(title, chunks):
    """Print a strategy's chunk count and a preview of each chunk."""
    print(f"\n{title}: {len(chunks)} chunks")
    for i, chunk in enumerate(chunks):
        print(f"  [{i}] {preview(chunk)}")


def main():
    print("Same document, three chunking strategies. Watch the boundaries.\n")
    print(f"Document: {len(DOCUMENT.split())} words, "
          f"{DOCUMENT.count(chr(10) * 2) + 1} paragraphs")

    show("Fixed-size (30 words, no overlap)", chunk_fixed(DOCUMENT, 30))
    show("Fixed-size (30 words, 8 overlap)", chunk_fixed(DOCUMENT, 30, overlap=8))
    show("Paragraph-based", chunk_paragraphs(DOCUMENT))

    print("\nTakeaway: overlap repeats text across chunks so ideas are not cut off;")
    print("paragraph splits respect natural boundaries but vary in size.")


if __name__ == "__main__":
    main()
