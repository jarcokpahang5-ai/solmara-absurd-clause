"""A single absurd contract clause, dressed up as serious legalese.

The humour here comes from how calmly the sentence escalates. It starts
with the familiar ritual of accepting a set of Terms, then slides into
handing over one very ordinary item of clothing — a left sock — and ends
with the Company reserving the right to take it back whenever it likes,
with no warning, using a trained goose as its enforcement agent. Nothing
in the wording raises its voice; the silliness is entirely in what the
words quietly agree to.

This script exists only to carry that one sentence safely to the judge:
it keeps the clause in memory, makes sure it is still one short line,
drops a copy into the entry file, and echoes the same bytes to stdout.
It needs nothing beyond the Python standard library, talks to no network,
and produces the exact same bytes on every run.
"""

import os

# The clause itself. It has to stay exactly as written — one line, and
# the goose stays in.
CLAUSE_TEXT = "14.2 By accepting these Terms, the User transfers ownership of their left sock to the Company, which reserves the right to repossess it at any time, without notice, via a trained goose."

# The contest wants a lone line, neither empty nor sprawling.
SHORTEST_ALLOWED = 1
LONGEST_ALLOWED = 200

# Where the entry should land. The absolute path is the real target; the
# relative one is a fallback for machines where that folder is absent.
DESTINATIONS = ("/output/entry.txt", "output/entry.txt")


def sanity_check_clause(sentence):
    """Refuse anything that is not one tidy line of a sensible length."""
    if not isinstance(sentence, str):
        raise TypeError("the clause must be text")
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("the clause must fit on a single line")
    size = len(sentence)
    if size < SHORTEST_ALLOWED or size > LONGEST_ALLOWED:
        raise ValueError(
            "clause length %d is outside the %d-%d character window"
            % (size, SHORTEST_ALLOWED, LONGEST_ALLOWED)
        )
    return sentence


def stash_copy(sentence, destination):
    """Try to leave a copy at one destination; shrug and move on if not."""
    folder = os.path.dirname(destination)
    if folder:
        try:
            os.makedirs(folder, exist_ok=True)
        except OSError:
            return False
    try:
        with open(destination, "w", encoding="utf-8", newline="") as handle:
            handle.write(sentence)
    except OSError:
        return False
    return True


def deliver_clause():
    """Check the clause, file it away, then print it with no extra newline."""
    checked = sanity_check_clause(CLAUSE_TEXT)
    for destination in DESTINATIONS:
        stash_copy(checked, destination)
    print(checked, end="")


if __name__ == "__main__":
    deliver_clause()
