"""The Absurd Clause Contest — make.fun bounty entry (u-donrulezz-the-absurd-clause-contest-035cc0f1).

The clause opens like ordinary boilerplate about accepting the Terms,
then quietly transfers ownership of the user's left sock to the Company —
and the repossession is carried out by a trained goose. The joke is the
deadpan escalation: a sock, a property transfer, and a goose, all in one clause of legalese.

Pure Python 3.13 standard library only. Deterministic, no network.
Writes the single entry line to /output/entry.txt (and to output/entry.txt
as a best effort) and prints it to stdout, byte-identical to the file.
"""

ENTRY = (
    "14.2 By accepting these Terms, the User transfers ownership of their left sock to the Company, which reserves the right to repossess it at any time, without notice, via a trained goose."
)


def main() -> None:
    text = ENTRY
    for path in ("/output/entry.txt", "output/entry.txt"):
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(text)
        except OSError:
            pass
    print(text, end="")


if __name__ == "__main__":
    main()
