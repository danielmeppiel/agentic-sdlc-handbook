#!/usr/bin/env python3
"""Post-process PDF and EPUB: remove the 'Download the Handbook' chapter.

This chapter is HTML-only (email gate form) and has no purpose in offline formats.
Quarto doesn't support per-format chapter lists, so we strip it after render.

Usage:
  python3 scripts/strip-blank-page.py _book/The-Agentic-SDLC-Handbook.pdf
  python3 scripts/strip-blank-page.py _book/The-Agentic-SDLC-Handbook.epub
"""
import sys
import os
import zipfile
import tempfile
import shutil
from xml.etree import ElementTree as ET


def fix_pdf(path):
    import fitz  # PyMuPDF
    doc = fitz.open(path)
    pages_to_remove = []

    for i in range(min(15, len(doc))):
        page = doc[i]
        text = page.get_text().strip()
        images = page.get_images()

        if not text and not images:
            pages_to_remove.append(i)
            print(f"  p{i+1}: blank — removing")
        elif not images and len(text) < 80 and "Download the Handbook" in text:
            pages_to_remove.append(i)
            print(f"  p{i+1}: stub '{text}' — removing")

    if not pages_to_remove:
        print(f"  PDF: no blank/stub pages — no change.")
        doc.close()
        return

    for i in reversed(pages_to_remove):
        doc.delete_page(i)

    toc = doc.get_toc()
    new_toc = [e for e in toc if "Download the Handbook" not in e[1]]
    if len(new_toc) != len(toc):
        doc.set_toc(new_toc)
        print(f"  Removed 'Download the Handbook' from TOC")

    doc.save(path, incremental=False, deflate=True, garbage=4)
    doc.close()
    print(f"  PDF: removed {len(pages_to_remove)} page(s)")


def fix_epub(path):
    tmpdir = tempfile.mkdtemp()
    try:
        # Extract
        with zipfile.ZipFile(path, "r") as zin:
            zin.extractall(tmpdir)

        # Find and remove the download chapter XHTML
        text_dir = os.path.join(tmpdir, "EPUB", "text")
        removed_file = None
        for fname in sorted(os.listdir(text_dir)):
            fpath = os.path.join(text_dir, fname)
            if not fname.endswith(".xhtml"):
                continue
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
            if "download-the-handbook" in content and "download-hero" in content:
                removed_file = fname
                os.remove(fpath)
                print(f"  Removed {fname} (download chapter)")
                break

        if not removed_file:
            print(f"  EPUB: no download chapter found — no change.")
            return

        # Update content.opf — remove the item and itemref
        opf_path = os.path.join(tmpdir, "EPUB", "content.opf")
        ET.register_namespace("", "http://www.idpf.org/2007/opf")
        ET.register_namespace("dc", "http://purl.org/dc/elements/1.1/")
        tree = ET.parse(opf_path)
        root = tree.getroot()
        ns = {"opf": "http://www.idpf.org/2007/opf"}

        # Find the item id for the removed file
        manifest = root.find("opf:manifest", ns)
        item_id = None
        for item in manifest.findall("opf:item", ns):
            if item.get("href") == f"text/{removed_file}":
                item_id = item.get("id")
                manifest.remove(item)
                print(f"  Removed manifest item: {item_id}")
                break

        # Remove from spine
        if item_id:
            spine = root.find("opf:spine", ns)
            for itemref in spine.findall("opf:itemref", ns):
                if itemref.get("idref") == item_id:
                    spine.remove(itemref)
                    print(f"  Removed spine itemref: {item_id}")
                    break

        tree.write(opf_path, xml_declaration=True, encoding="UTF-8")

        # Update nav.xhtml — remove the download entry from TOC
        nav_path = os.path.join(tmpdir, "EPUB", "nav.xhtml")
        if os.path.exists(nav_path):
            with open(nav_path, "r", encoding="utf-8") as f:
                nav = f.read()
            # Remove the <li> containing the download link
            import re
            nav = re.sub(
                r'<li[^>]*>\s*<a[^>]*href="text/' + removed_file + r'"[^>]*>.*?</a>\s*</li>\s*',
                "", nav, flags=re.DOTALL
            )
            with open(nav_path, "w", encoding="utf-8") as f:
                f.write(nav)
            print(f"  Cleaned nav.xhtml")

        # Repack EPUB
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as zout:
            # mimetype must be first and uncompressed
            mimetype_path = os.path.join(tmpdir, "mimetype")
            if os.path.exists(mimetype_path):
                zout.write(mimetype_path, "mimetype", compress_type=zipfile.ZIP_STORED)

            for root_dir, dirs, files in os.walk(tmpdir):
                for fname in files:
                    full = os.path.join(root_dir, fname)
                    arcname = os.path.relpath(full, tmpdir)
                    if arcname == "mimetype":
                        continue
                    zout.write(full, arcname)

        print(f"  EPUB: repacked successfully")

    finally:
        shutil.rmtree(tmpdir)


def main():
    if len(sys.argv) < 2:
        print("Usage: strip-blank-page.py <pdf-or-epub-path>")
        sys.exit(1)

    path = sys.argv[1]
    if path.endswith(".pdf"):
        fix_pdf(path)
    elif path.endswith(".epub"):
        fix_epub(path)
    else:
        print(f"Unknown format: {path}")
        sys.exit(1)


if __name__ == "__main__":
    main()
