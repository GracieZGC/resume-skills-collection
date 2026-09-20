"""Prompt-eval harness for the Resume Optimizer skill.

Loads the skill body, runs each YAML case in ./cases against Claude, and
evaluates simple structural assertions on the response. Exits non-zero on
any failure.

If ANTHROPIC_API_KEY is unset, the harness exits 0 with a "skipped" message.
This lets CI run lint without API access.

Usage:
    python eval_harness.py            # run every case under cases/
    python eval_harness.py case-name  # run one case (no extension)
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from typing import Any

import yaml  # type: ignore[import-untyped]

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
SKILL_PATH = REPO / "skill" / "SKILL.md"
CASES_DIR = ROOT / "cases"


def load_skill() -> str:
    """Strip the YAML frontmatter — we only want the body as a system message."""
    text = SKILL_PATH.read_text(encoding="utf-8")
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end >= 0:
            text = text[end + 4 :].lstrip()
    return text


def load_fixture(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8")


def build_user_message(prompt: str, inputs: dict[str, Any] | None) -> str:
    """Render the prompt, appending any resume fixture under a clear heading."""
    msg = prompt.rstrip()
    if not inputs:
        return msg
    resume_path = inputs.get("resume")
    if resume_path:
        resume = load_fixture(resume_path)
        msg += f"\n\nHere is the resume:\n\n```\n{resume}\n```\n"
    return msg


def evaluate_assertions(response: str, assertions: list[dict[str, Any]]) -> list[str]:
    """Return a list of failure messages (empty list = all passed)."""
    failures: list[str] = []
    for a in assertions:
        if "contains" in a:
            pattern = a["contains"]
            if not re.search(pattern, response):
                failures.append(f"  - assertion failed: contains {pattern!r}")
        elif "not_contains" in a:
            pattern = a["not_contains"]
            if re.search(pattern, response):
                failures.append(f"  - assertion failed: not_contains {pattern!r}")
        elif "section_present" in a:
            heading = a["section_present"]
            # Heading must appear on its own line (anchored).
            if not re.search(rf"^{re.escape(heading)}\s*$", response, flags=re.MULTILINE):
                failures.append(f"  - assertion failed: section_present {heading!r}")
        else:
            failures.append(f"  - unknown assertion: {a!r}")
    return failures


def call_claude(system: str, user: str) -> str:
    # Imported lazily so the harness can be parsed/inspected without the SDK installed.
    from anthropic import Anthropic  # type: ignore[import-not-found]

    client = Anthropic()
    response = client.messages.create(
        model=os.environ.get("RESUME_OPTIMIZER_TEST_MODEL", "claude-opus-4-7"),
        max_tokens=4096,
        system=system,
        messages=[{"role": "user", "content": user}],
    )
    # Concatenate all text blocks.
    parts: list[str] = []
    for block in response.content:
        if getattr(block, "type", None) == "text":
            parts.append(block.text)  # type: ignore[attr-defined]
    return "\n".join(parts)


def run_case(case_path: Path, system: str) -> bool:
    """Run one YAML case. Returns True on pass, False on fail."""
    data = yaml.safe_load(case_path.read_text(encoding="utf-8"))
    name = data.get("name", case_path.stem)
    user = build_user_message(data["prompt"], data.get("inputs"))
    response = call_claude(system, user)
    failures = evaluate_assertions(response, data.get("assertions", []))
    if failures:
        print(f"FAIL: {name}")
        for line in failures:
            print(line)
        return False
    print(f"PASS: {name}")
    return True


def main(argv: list[str]) -> int:
    if "ANTHROPIC_API_KEY" not in os.environ:
        print("ANTHROPIC_API_KEY not set — skipping prompt-eval suite.")
        return 0

    system = load_skill()
    if argv[1:]:
        targets = [CASES_DIR / f"{n}.yaml" for n in argv[1:]]
    else:
        targets = sorted(CASES_DIR.glob("*.yaml"))

    if not targets:
        print("No cases found.")
        return 1

    failed = 0
    for path in targets:
        if not run_case(path, system):
            failed += 1
    if failed:
        print(f"\n{failed} of {len(targets)} cases failed.")
        return 1
    print(f"\nAll {len(targets)} cases passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
