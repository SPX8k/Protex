from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from validate_skill import parse_frontmatter, validate_skill


class ParseFrontmatterTests(unittest.TestCase):
    def test_parses_metadata_and_body(self) -> None:
        metadata, body = parse_frontmatter(
            "---\nname: protex\ndescription: Safe project changes.\n---\n\nBody.\n"
        )
        self.assertEqual(metadata["name"], "protex")
        self.assertEqual(metadata["description"], "Safe project changes.")
        self.assertIn("Body.", body)

    def test_rejects_missing_opening_delimiter(self) -> None:
        with self.assertRaisesRegex(ValueError, "beginnen"):
            parse_frontmatter("name: protex\n---\nBody")

    def test_rejects_missing_closing_delimiter(self) -> None:
        with self.assertRaisesRegex(ValueError, "schließenden"):
            parse_frontmatter("---\nname: protex\ndescription: Test")


class ValidateSkillTests(unittest.TestCase):
    def test_repository_skill_passes(self) -> None:
        skill_dir = PROJECT_ROOT / ".agents" / "skills" / "protex"
        self.assertEqual(validate_skill(skill_dir), [])

    def test_missing_skill_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            errors = validate_skill(Path(directory))
        self.assertEqual(len(errors), 1)
        self.assertIn("SKILL.md", errors[0])

    def test_invalid_name_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            skill_dir = Path(directory)
            (skill_dir / "agents").mkdir()
            (skill_dir / "references").mkdir()
            for relative in (
                "agents/openai.yaml",
                "references/safe-file-operations.md",
                "references/testing-and-verification.md",
            ):
                (skill_dir / relative).write_text("present", encoding="utf-8")
            (skill_dir / "agents" / "openai.yaml").write_text(
                "display_name: Protex\nshort_description: Test\ndefault_prompt: Test\n",
                encoding="utf-8",
            )
            content = (
                "---\nname: Not_Valid\ndescription: Test\n---\n"
                + "\n".join(REQUIRED_HEADINGS_FOR_TESTS)
                + "\nfrage vor der erweiterung nach freigabe\nvor jeder riskanten operation\n"
                + "tatsächlich testen\nbehaupte nicht\nlösche, verschiebe\n"
            )
            (skill_dir / "SKILL.md").write_text(content, encoding="utf-8")
            errors = validate_skill(skill_dir)
        self.assertTrue(any("name muss" in error for error in errors))


REQUIRED_HEADINGS_FOR_TESTS = (
    "## 1. Grundhaltung",
    "## 2. Den Änderungsumfang respektieren",
    "## 3. Dateien schützen",
    "## 4. In klaren Schritten arbeiten",
    "## 5. Vollständigkeit",
    "## 6. Abschließende Selbstprüfung",
    "## 7. Grenzen",
)


if __name__ == "__main__":
    unittest.main()
