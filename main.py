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
    outDir = "/output"
    import os
    os.makedirs(outDir, exist_ok=True)
    with open(os.path.join(outDir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote entry ({len(ENTRY)} chars) to {outDir}/entry.txt")


if __name__ == "__main__":
    main()
