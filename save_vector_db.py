#!/usr/bin/env python3
"""
Save Vector Database to File
Demonstrate file persistence for ChromaDB
"""

import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import json
import os
from utils import read_casadeanza_docs

print("💾 Saving Vector Database to File")
print("=" * 50)

# Initialize ChromaDB and model
print("1. Setting up vector database...")
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection("casadeanza_docs")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("   ✅ Persistent ChromaDB and model ready")

# Add documents from CasaDeAnza files
print("2. Loading CasaDeAnza documents...")
docs, paths = read_casadeanza_docs()

if not docs:
    print("   ⚠️ No CasaDeAnza documents found. Using sample fallback.")
    sample_docs = [
        "CasaDeAnza Equipment Reimbursement Policy - Receipts must be submitted within 30 days of purchase.",
        "CasaDeAnza allows remote work up to 3 days per week",
        "CasaDeAnza's Patios and Balconies rules prohibit hanging items over railings."
    ]
    paths = [f"sample_{i+1}" for i in range(len(sample_docs))]
else:
    sample_docs = docs

collection.add(
    documents=sample_docs,
    ids=[os.path.splitext(os.path.basename(p))[0] for p in paths],
    metadatas=[{"source": os.path.basename(p)} for p in paths]
)
print(f"   ✅ Added {len(sample_docs)} documents")

# Save collection data to file
print("3. Saving to file...")
collection_data = {
    "documents": sample_docs,
    "ids": [os.path.splitext(os.path.basename(p))[0] for p in paths],
    "sources": [os.path.basename(p) for p in paths],
    "count": len(sample_docs)
}

# Save as JSON file
with open("vectordb_backup.json", "w") as f:
    json.dump(collection_data, f, indent=2)

print("   ✅ Saved to vectordb_backup.json")

# Verify file was created
if os.path.exists("vectordb_backup.json"):
    file_size = os.path.getsize("vectordb_backup.json")
    print(f"   ✅ File size: {file_size} bytes")

print()
print("💡 File Persistence Benefits:")
print("✅ Data survives system restarts")
print("✅ Can be shared between applications")
print("✅ Backup and restore capabilities")
print("✅ Version control for document changes")

print()
print("🎉 Vector Database Saved Successfully!")
print(f"📊 Documents saved: {len(sample_docs)}")
print(f"📊 File: vectordb_backup.json")
print(f"📊 File size: {file_size} bytes")

# Create completion marker
with open("vectordb_saved.txt", "w") as f:
    f.write("Vector database saved to file successfully")

print("✅ File persistence complete!")
