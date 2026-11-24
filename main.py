"""Entry for make.fun bounty: The Long Roast: Lawmakers and the File They
Cannot Convert (u-swift-raven-16-the-long-roast-lawmakers-and-the-f3a3bdf7).

Writes one satirical sentence (1-320 characters) to /output/entry.txt
(and ./entry.txt for local verification). Stdlib only, no network,
deterministic: the same sentence every run. Gate: 1-320 chars, one sentence.
"""

import os

SENTENCE = (
    "The senator who would ban your crypto wallet still emails his aide a "
    "file called FINAL_final_v2.docx and asks her to turn it into a PDF."
)


def main():
    for path in ("/output/entry.txt", "entry.txt"):
        directory = os.path.dirname(path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(SENTENCE)


if __name__ == "__main__":
    main()
