"""
Structural integrity tests for bestiary/BESTIARY.md.

The document defines the Bestiary — Mythological Beings as Interactive Entities.
These tests verify that every defined schema, section, entity, and expected structural
element is present and complete.
"""
import unittest
from pathlib import Path

BESTIARY_FILE = Path(__file__).parent.parent / "bestiary" / "BESTIARY.md"

class TestBestiaryFileExists(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(BESTIARY_FILE.exists(), f"Expected bestiary file at {BESTIARY_FILE}")

    def test_file_is_not_empty(self):
        self.assertGreater(BESTIARY_FILE.stat().st_size, 0, "Bestiary file must not be empty")

class TestDocumentStructure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = BESTIARY_FILE.read_text(encoding="utf-8")
        cls.lines = cls.content.splitlines()

    def test_starts_with_h1_heading(self):
        self.assertTrue(
            self.lines[0].startswith("# "),
            "Document must begin with an H1 heading",
        )

    def test_title_references_bestiary(self):
        self.assertIn("BESTIARY", self.lines[0].upper(), "H1 title must reference BESTIARY")

    def test_entity_schema_present(self):
        self.assertIn("## Entity Schema", self.content, "## Entity Schema section must be present")

    def test_schema_is_yaml(self):
        start = self.content.find("## Entity Schema")
        block_start = self.content.find("```yaml", start)
        self.assertNotEqual(block_start, -1, "A yaml code block must exist under Entity Schema")

    def test_schema_keys_present(self):
        keys = ["name:", "tradition:", "allegiance:", "type:", "realm:", "encounter_conditions:", "behavior:", "powers:", "weakness:", "narrative_role:"]
        for key in keys:
            with self.subTest(key=key):
                self.assertIn(key, self.content, f"Schema must include '{key}'")

class TestBestiarySections(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = BESTIARY_FILE.read_text(encoding="utf-8")

    def test_founding_bestiary_entries_heading(self):
        self.assertIn("## Founding Bestiary Entries", self.content)

    def test_categories_present(self):
        categories = ["### Guardians", "### Tricksters", "### Sovereigns", "### Heralds", "### Monsters", "### Sages", "### Artifacts"]
        for category in categories:
            with self.subTest(category=category):
                self.assertIn(category, self.content, f"Category '{category}' must be present")

class TestBestiaryEntities(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = BESTIARY_FILE.read_text(encoding="utf-8")

    def test_guardians_present(self):
        entities = ["**The Bridge Keeper**", "**The Custodian**"]
        for entity in entities:
            with self.subTest(entity=entity):
                self.assertIn(entity, self.content, f"Guardian '{entity}' must be present")

    def test_tricksters_present(self):
        entities = ["**The Virus in Sunglasses**", "**The Trickster Spider**"]
        for entity in entities:
            with self.subTest(entity=entity):
                self.assertIn(entity, self.content, f"Trickster '{entity}' must be present")

    def test_sovereigns_present(self):
        entities = ["**The Delegated King**", "**The Pressure Lord**"]
        for entity in entities:
            with self.subTest(entity=entity):
                self.assertIn(entity, self.content, f"Sovereign '{entity}' must be present")

    def test_heralds_present(self):
        entities = ["**The Psychopomp Ferryman**", "**The Deck Reader**"]
        for entity in entities:
            with self.subTest(entity=entity):
                self.assertIn(entity, self.content, f"Herald '{entity}' must be present")

    def test_monsters_present(self):
        entities = ["**The Phaethon**", "**The Taint**"]
        for entity in entities:
            with self.subTest(entity=entity):
                self.assertIn(entity, self.content, f"Monster '{entity}' must be present")

    def test_sages_present(self):
        entities = ["**The Old Wizard**"]
        for entity in entities:
            with self.subTest(entity=entity):
                self.assertIn(entity, self.content, f"Sage '{entity}' must be present")

    def test_artifacts_present(self):
        entities = ["**The Deck of Dragons**", "**The Chronicle Tablet**"]
        for entity in entities:
            with self.subTest(entity=entity):
                self.assertIn(entity, self.content, f"Artifact '{entity}' must be present")

if __name__ == "__main__":
    unittest.main(verbosity=2)
