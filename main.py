"""Write the one word to erase from the dictionary to entry.txt.

The entry is a single word, written exactly as chosen, with no trailing
newline and nothing else attached.

The chosen word is pneumonoultramicroscopicsilicovolcanoconiosis: the
45-letter name of a lung disease caused by inhaling very fine volcanic
dust. It is the longest word in major dictionaries, and nobody can spell
it, pronounce it, or has ever needed to say it -- deleting it changes
nothing, and that is the joke. The humour comes from the word itself:
its absurd length, its unpronounceability, and the zero-sized gap its
absence would leave in the language.
"""

import os

# The one word to erase from the dictionary forever.
WORD = "pneumonoultramicroscopicsilicovolcanoconiosis"

# Gate limits from the competition rules: entry.txt must be UTF-8 text
# of 1 to 77 characters, not only whitespace. The chosen word is 45
# characters, comfortably inside that window.
MIN_CHARS = 1
MAX_CHARS = 77


def validate(word: str) -> None:
    """Check the entry against the gate before anything is written."""
    if not isinstance(word, str):
        raise TypeError("entry must be a string")
    if not MIN_CHARS <= len(word) <= MAX_CHARS:
        raise ValueError(f"entry must be {MIN_CHARS}-{MAX_CHARS} characters")
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if word != word.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    word.encode("utf-8")


def main() -> None:
    validate(WORD)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
