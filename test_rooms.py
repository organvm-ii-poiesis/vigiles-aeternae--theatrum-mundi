import os
import unittest

class TestHereThereEverywhereNowhere(unittest.TestCase):
    def setUp(self):
        self.filepath = "rooms/primary/here-there-everywhere-nowhere.md"

    def test_file_exists(self):
        self.assertTrue(os.path.exists(self.filepath), "The largest source module must exist")

    def test_file_not_empty(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertGreater(len(content), 0, "The module should not be empty")

    def test_contains_required_sections(self):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertIn("# :HERE.THERE.EVERYWHERE.NOWHERE", content)
        self.assertIn("## Summary", content)

if __name__ == '__main__':
    unittest.main()
