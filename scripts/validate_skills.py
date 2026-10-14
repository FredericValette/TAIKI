import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "SKILL.md",
    "prompts/assessment.prompt.md",
    "references/output-contract.md",
    "schemas/input.schema.json",
    "examples/input.json",
)


def validate_skills():
    skill_directories = sorted(path for path in (ROOT / "skills").iterdir() if path.is_dir())
    errors = []

    if len(skill_directories) != 11:
        errors.append(f"Expected 11 skills, found {len(skill_directories)}")

    for skill_directory in skill_directories:
        skill_file = skill_directory / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"{skill_directory.name}: missing SKILL.md")
            continue

        content = skill_file.read_text(encoding="utf-8")
        declared_name = next(
            (line.removeprefix("name:").strip() for line in content.splitlines() if line.startswith("name:")),
            None,
        )
        if declared_name != skill_directory.name:
            errors.append(f"{skill_directory.name}: frontmatter name does not match directory")

        for relative_path in REQUIRED_FILES:
            artifact = skill_directory / relative_path
            if not artifact.is_file():
                errors.append(f"{skill_directory.name}: missing {relative_path}")
                continue
            if artifact.suffix == ".json":
                try:
                    json.loads(artifact.read_text(encoding="utf-8"))
                except json.JSONDecodeError as error:
                    errors.append(f"{skill_directory.name}: invalid {relative_path}: {error}")

    return errors


if __name__ == "__main__":
    validation_errors = validate_skills()
    if validation_errors:
        print("\n".join(validation_errors), file=sys.stderr)
        sys.exit(1)
    print("Validated 11 skill packages.")