#!/usr/bin/env python3
"""
Common utilities for RAG search methods
"""

import os
import glob
import PyPDF2

directory = "./casadeanza-proj"  # Change to your target folder


def find_pdfs(directory):
    """
    Find all PDF files in the given directory (case-insensitive).
    """
    # Match both .pdf and .PDF (case-insensitive)
    pattern_lower = os.path.join(directory, "*.pdf")
    pattern_upper = os.path.join(directory, "*.PDF")
    
    pdf_files = glob.glob(pattern_lower) + glob.glob(pattern_upper)
    return sorted(set(pdf_files))  # Remove duplicates and sort

def read_pdf(file_path):
    """
    Read text from a PDF file safely.
    """
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page_num, page in enumerate(reader.pages):
                try:
                    text += page.extract_text() or ""
                except Exception as e:
                    print(f"⚠️ Could not read page {page_num} in {file_path}: {e}")
            return text.strip()
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
    except PyPDF2.errors.PdfReadError as e:
        print(f"❌ Error reading PDF {file_path}: {e}")
    except Exception as e:
        print(f"❌ Unexpected error with {file_path}: {e}")
    return None



def read_casadeanza_docs():
    """Read all PDF documents from casadeanza-proj directory"""
    docs = []
    doc_paths = []
    
    # Find all PDF files in the directory
    pdf_files = find_pdfs(directory)
    
    for file_path in pdf_files:
        content = read_pdf(file_path)
        if content:  # Only add non-empty files
            docs.append(content)
            doc_paths.append(file_path)
    
    return docs, doc_paths

def get_casadeanza_doc_info():
    """Get document information for display"""
    docs, paths = read_casadeanza_docs()
    
    print(f"📚 Loaded {len(docs)} documents")
    print("\nDocuments:")
    for i, (doc, path) in enumerate(zip(docs, paths)):
        print(f"{i+1}. [{path}] - {len(doc)} characters")
    
    return docs, paths


if __name__ == "__main__":
    directory = "./casadeanza-proj"  # Change to your target folder
    pdf_files = find_pdfs(directory)

    if not pdf_files:
        print("No PDF files found.")
    else:
        for pdf in pdf_files:
            print(f"\n📄 Reading: {pdf}")
            content = read_pdf(pdf)
            if content:
                print(f"--- First 300 characters ---\n{content[:300]}")


