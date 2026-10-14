import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
REQUIRED_FILES = (
    "SKILL.md",
    "prompts/assessment.prompt.md",
    "references/output-contract.md",
    "schemas/input.schema.json",
    "examples/input.json",
)


class SkillPackageTests(unittest.TestCase):
    def test_every_skill_has_the_required_package_files(self):
        skills = sorted(path for path in (ROOT / "skills").iterdir() if path.is_dir())
        self.assertEqual(len(skills), 11)
        for skill in skills:
            with self.subTest(skill=skill.name):
                for relative_path in REQUIRED_FILES:
                    self.assertTrue((skill / relative_path).is_file(), relative_path)


if __name__ == "__main__":
    unittest.main()