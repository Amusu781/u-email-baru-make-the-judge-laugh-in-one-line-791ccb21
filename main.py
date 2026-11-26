"""Make the Judge Laugh in One Line — entry program.

Writes a single original one-line joke to entry.txt in the output
directory (``/output`` by default, or ``$MAKEFUN_OUTPUT_DIR``).

The line is validated before it is written: it must be 1-200 characters,
a single line, and not only whitespace.
"""

import os
import shutil

LINE = (
    "My fitness tracker congratulated me on 10,000 steps \u2014 "
    "I'd just been pacing outside the fridge for an hour."
)


def validate_line(line: str) -> None:
    """Check the line meets the sealed gate: 1-200 chars, one line, non-blank."""
    assert isinstance(line, str), "line must be a string"
    assert 1 <= len(line) <= 200, "line must be 1-200 characters"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"
    assert line == line.strip(), "line must not start or end with whitespace"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

    # Create the output directory first, before writing anything.
    os.makedirs(output_dir, exist_ok=True)

    # Clear only the contents of the output directory, never the
    # directory itself (the grader mounts it read-only as uid 65534).
    for name in os.listdir(output_dir):
        path = os.path.join(output_dir, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)

    # Validate the line before writing.
    validate_line(LINE)

    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
