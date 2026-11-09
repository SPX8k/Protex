#!/usr/bin/env python3
"""Validate the Protex Agent Skill using only the Python standard library."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_HEADINGS = (
    "## 1. Grundhaltung",
    "## 2. Den Änderungsumfang respektieren",
    "## 3. Dateien schützen",
    "## 4. In klaren Schritten arbeiten",
    "## 5. Vollständigkeit",
    "## 6. Abschließende Selbstprüfung",
    "## 7. Grenzen",
)
REQUIRED_REFERENCES = (
    "references/safe-file-operations.md",
    "references/testing-and-verification.md",
    "agents/openai.yaml",
)
REQUIRED_TERMS = (
    "frage vor der erweiterung nach freigabe",
    "vor jeder riskanten operation",
    "tatsächlich testen",
    "behaupte nicht",
    "lösche, verschiebe",
)


def parse_frontmatter(content: str) -> tuple[dict[str, str], str]:
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("SKILL.md muss mit YAML-Frontmatter beginnen.")

    try:
        end = next(i for i, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration as exc:
        raise ValueError("YAML-Frontmatter hat keinen schließenden Trenner.") from exc

    metadata: dict[str, str] = {}
    for number, line in enumerate(lines[1:end], start=2):
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"Ungültige Frontmatter-Zeile {number}: {line}")
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if not key or not value:
            raise ValueError(f"Leerer Schlüssel oder Wert in Zeile {number}.")
        if len(value) >= 2 and value[0] in "\"'" and value[-1] == value[0]:
            value = value[1:-1]
        metadata[key] = value

    return metadata, "\n".join(lines[end + 1:])


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"Pflichtdatei fehlt: {skill_file}"]

    try:
        content = skill_file.read_text(encoding="utf-8")
        metadata, body = parse_frontmatter(content)
    except (OSError, UnicodeError, ValueError) as exc:
        return [str(exc)]

    name = metadata.get("name", "")
    description = metadata.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append("name muss 1–64 Zeichen haben und dem Skill-Namensformat entsprechen.")
    if not description or len(description) > 1024:
        errors.append("description muss vorhanden sein und höchstens 1024 Zeichen haben.")

    for heading in REQUIRED_HEADINGS:
        if heading not in body:
            errors.append(f"Abschnitt fehlt: {heading}")

    lowered = body.casefold()
    for term in REQUIRED_TERMS:
        if term not in lowered:
            errors.append(f"Schutzregel fehlt: {term}")

    for relative in REQUIRED_REFERENCES:
        if not (skill_dir / relative).is_file():
            errors.append(f"Referenzdatei fehlt: {relative}")

    agent_config = skill_dir / "agents" / "openai.yaml"
    if agent_config.is_file():
        config = agent_config.read_text(encoding="utf-8")
        for field in ("display_name:", "short_description:", "default_prompt:"):
            if field not in config:
                errors.append(f"agents/openai.yaml: Pflichtfeld fehlt: {field}")

    if any(marker in content for marker in ("TODO", "[REST EINFÜGEN]", "HIER CODE EINFÜGEN")):
        errors.append("SKILL.md enthält einen nicht aufgelösten Platzhalter.")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Prüft die Protex-Skill-Dateien.")
    parser.add_argument(
        "--skill-dir",
        type=Path,
        default=Path(__file__).resolve().parents[1] / ".agents" / "skills" / "protex",
    )
    args = parser.parse_args()
    errors = validate_skill(args.skill_dir.resolve())

    if errors:
        print("Protex-Validierung fehlgeschlagen:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Protex-Validierung bestanden: {args.skill_dir.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
