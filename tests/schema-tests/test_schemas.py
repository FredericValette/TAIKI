import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator
from referencing import Registry, Resource


ROOT = Path(__file__).resolve().parents[2]


class SchemaContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schema_paths = sorted((ROOT / "controller" / "schemas").glob("*.schema.json"))
        cls.schema_paths.extend(sorted((ROOT / "skills").glob("*/schemas/*.schema.json")))
        cls.schemas = {
            path: json.loads(path.read_text(encoding="utf-8")) for path in cls.schema_paths
        }
        resources = [
            (schema["$id"], Resource.from_contents(schema))
            for schema in cls.schemas.values()
            if "$id" in schema
        ]
        cls.registry = Registry().with_resources(resources)

    def test_all_schemas_are_valid_draft_2020_12(self):
        self.assertTrue(self.schema_paths)
        for schema in self.schemas.values():
            with self.subTest(schema=schema.get("title")):
                Draft202012Validator.check_schema(schema)

    def test_skill_examples_validate_against_their_input_schemas(self):
        for schema_path, schema in self.schemas.items():
            if schema_path.parts[-3] != "schemas":
                continue
            if schema_path.parts[0] == "skills":
                example_path = schema_path.parents[1] / "examples" / "input.json"
                instance = json.loads(example_path.read_text(encoding="utf-8"))
                validator = Draft202012Validator(schema, registry=self.registry)
                with self.subTest(skill=schema_path.parts[1]):
                    validator.validate(instance)

    def test_controller_run_example_validates_with_referenced_contracts(self):
        schema_path = ROOT / "controller" / "schemas" / "controller-run.schema.json"
        schema = self.schemas[schema_path]
        instance = json.loads((ROOT / "examples" / "controller-run.json").read_text(encoding="utf-8"))
        Draft202012Validator(schema, registry=self.registry).validate(instance)


if __name__ == "__main__":
    unittest.main()