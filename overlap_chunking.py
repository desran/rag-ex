#!/usr/bin/env python3
"""
Overlap Chunking Demo
Demonstrates the importance of overlap for context preservation
"""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from utils import read_casadeanza_docs

print("✂️ Overlap Chunking Demo")
print("=" * 50)

# Load documents from the casadeanza project PDFs. Use the first PDF as
# the sample document for this demo. If no PDFs are found, fall back to
# a small embedded sample to keep the demo runnable.

docs, doc_paths = read_casadeanza_docs()
if docs:
    sample_document = docs[0]
    sample_source = doc_paths[0]
    print(f"📄 Using first PDF document: {sample_source}")
else:
    sample_document = """
CasaDeAnza Equipment Reimbursement Policy

Section 1: Reimbursement Process
Receipts must be submitted within 30 days of purchase. Use the company expense reporting system to submit your claim. Include original receipts and manager approval email. Reimbursement will be processed within 2 weeks of submission.

"""
    print("📄 No PDFs found — using embedded sample document.")

print(f"Length: {len(sample_document)} characters")
print()

# Test 1: Chunking WITHOUT overlap
print("🔧 Test 1: Chunking WITHOUT Overlap")
print("-" * 40)

splitter_no_overlap = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=0,  # No overlap
    separators=["\n\n", "\n", " ", ""]
)

chunks_no_overlap = splitter_no_overlap.split_text(sample_document)

print(f"Created {len(chunks_no_overlap)} chunks without overlap:")
for i, chunk in enumerate(chunks_no_overlap, 1):
    print(f"Chunk {i}: {chunk[:80]}...")
print()

# Test 2: Chunking WITH overlap
print("🔧 Test 2: Chunking WITH Overlap")
print("-" * 40)

splitter_with_overlap = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,  # 50 character overlap
    separators=["\n\n", "\n", " ", ""]
)

chunks_with_overlap = splitter_with_overlap.split_text(sample_document)

print(f"Created {len(chunks_with_overlap)} chunks with overlap:")
for i, chunk in enumerate(chunks_with_overlap, 1):
    print(f"Chunk {i}: {chunk[:80]}...")
print()



