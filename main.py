"""Have You Tried Turning It Off? — make.fun bounty entry.

Writes one funny line spoken by a desperate tech support agent to a
desperate customer, to /output/entry.txt.
"""

ENTRY = "Have you tried turning it off and on again? No? Then have you tried turning yourself off and on again \u2014 the problem might be you."


def main():
    if len(ENTRY) >= 200:
        raise ValueError(f"Entry must be under 200 characters, got {len(ENTRY)}")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("Entry must be a single line")
    if not ENTRY.strip():
        raise ValueError("Entry must not be empty or whitespace only")
    if ENTRY != ENTRY.strip():
        raise ValueError("Entry must not have leading or trailing whitespace")
    if any(ord(ch) < 32 and ch not in ("\t",) for ch in ENTRY):
        raise ValueError("Entry must not contain control characters")
    if not ENTRY.isprintable():
        raise ValueError("Entry must contain only printable characters")
    if "  " in ENTRY:
        raise ValueError("Entry must not contain double spaces")
    outDir = "/output"
    import os
    import tempfile
    os.makedirs(outDir, exist_ok=True)
    outPath = os.path.join(outDir, "entry.txt")
    fd, tmpPath = tempfile.mkstemp(dir=outDir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(ENTRY + "\n")
        os.replace(tmpPath, outPath)
    except BaseException:
        try:
            os.unlink(tmpPath)
        except OSError:
            pass
        raise
    with open(outPath, "r", encoding="utf-8") as f:
        written = f.read().rstrip("\n")
    if written != ENTRY:
        raise ValueError("Written entry does not match expected entry")
    if len(written.splitlines()) != 1:
        raise ValueError("Written entry must be exactly one line")
    print(f"Wrote entry ({len(ENTRY)} chars) to {outDir}/entry.txt")


if __name__ == "__main__":
    main()
