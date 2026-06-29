"""
Structural integrity tests for rooms/primary/here-there-everywhere-nowhere.md.

The document defines the H.E.R.E./T.H.E.R.E./E.V.E.R.Y.W.H.E.R.E. recursive room
system (rooms AA09–AA16) used as the spatial navigation layer of the Vigiles Aeternae
world-OS. These tests verify that every defined room, protocol, function, and structural
element is present and complete.
"""
import re
import unittest
from pathlib import Path

ROOM_FILE = (
    Path(__file__).parent.parent
    / "rooms"
    / "primary"
    / "here-there-everywhere-nowhere.md"
)


class TestRoomFileExists(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(ROOM_FILE.exists(), f"Expected room file at {ROOM_FILE}")

    def test_file_is_not_empty(self):
        self.assertGreater(ROOM_FILE.stat().st_size, 0, "Room file must not be empty")


class TestDocumentStructure(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = ROOM_FILE.read_text(encoding="utf-8")
        cls.lines = cls.content.splitlines()

    def test_starts_with_h1_heading(self):
        self.assertTrue(
            self.lines[0].startswith("# "),
            "Document must begin with an H1 heading",
        )

    def test_title_references_here(self):
        self.assertIn("HERE", self.lines[0].upper(), "H1 title must reference HERE")

    def test_summary_section_present(self):
        self.assertIn("## Summary", self.content, "## Summary section must be present")

    def test_export_header_present(self):
        self.assertIn(
            "WORLD.OS // THREAD EXPORT HEADER",
            self.content,
            "Thread export header block must be present",
        )

    def test_thread_id_present(self):
        self.assertIn(
            "THRD_AA09_REC_OS",
            self.content,
            "Thread ID THRD_AA09_REC_OS must be stamped in the document",
        )


class TestMermaidDiagram(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = ROOM_FILE.read_text(encoding="utf-8")

    def test_mermaid_block_present(self):
        self.assertIn("```mermaid", self.content, "A mermaid code block must exist")

    def test_mermaid_is_flowchart(self):
        start = self.content.find("```mermaid")
        end = self.content.find("```", start + 10)
        block = self.content[start:end]
        self.assertIn("flowchart TD", block, "Mermaid block must declare 'flowchart TD'")

    def test_mermaid_block_closed(self):
        open_count = self.content.count("```mermaid")
        closed = 0
        pos = 0
        while True:
            start = self.content.find("```mermaid", pos)
            if start == -1:
                break
            end = self.content.find("```", start + 10)
            if end != -1:
                closed += 1
            pos = start + 10
        self.assertEqual(open_count, closed, "Every mermaid block must be closed")

    def test_here_acronym_nodes_in_diagram(self):
        start = self.content.find("```mermaid")
        end = self.content.find("```", start + 10)
        block = self.content[start:end]
        for letter in ["Harmonic", "Event", "Recursive", "Echo"]:
            with self.subTest(letter=letter):
                self.assertIn(letter, block, f"Mermaid diagram must include '{letter}'")


class TestHEREProtocol(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = ROOM_FILE.read_text(encoding="utf-8")

    def test_here_acronym_defined(self):
        """H.E.R.E. = Harmonic Event Recursive Echo."""
        for word in ("Harmonic", "Recursive", "Echo"):
            with self.subTest(word=word):
                self.assertIn(word, self.content, f"H.E.R.E. expansion must include '{word}'")

    def test_protocol_4d_flattening_named(self):
        self.assertIn(
            "4D.FLATTENING",
            self.content,
            "Primary protocol 4D.FLATTENING must be named",
        )

    def test_here_effects_upon_activation(self):
        effects = [
            "Temporal collapse",
            "Spatial recursion",
            "Symbol ignition",
            "Canon fracture",
        ]
        for effect in effects:
            with self.subTest(effect=effect):
                self.assertIn(effect, self.content, f"Effect '{effect}' must be listed")

    def test_here_recursive_function_defined(self):
        self.assertIn("def HERE", self.content, "HERE(time) recursive function must be defined")


class TestPrimaryRooms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = ROOM_FILE.read_text(encoding="utf-8")

    PRIMARY_ROOMS = [
        ("AA09", "H.E.R.E"),
        ("AA10", "T.H.E.R.E"),
        ("AA11", "E.V.E.R.Y.W.H.E.R.E"),
        ("AA12", "M41N_STR33T"),
    ]

    def test_room_cluster_heading_present(self):
        self.assertIn(
            "ROOM_CLUSTER_AA09",
            self.content,
            "Room cluster ROOM_CLUSTER_AA09 must be declared",
        )

    def test_all_primary_room_ids_present(self):
        for room_id, room_name in self.PRIMARY_ROOMS:
            with self.subTest(room=room_name):
                self.assertIn(room_id, self.content, f"Room ID {room_id} must appear")
                self.assertIn(room_name, self.content, f"Room name {room_name} must appear")

    def test_here_core_functions_table_present(self):
        self.assertIn(
            "CORE FUNCTIONS IN ROOM",
            self.content,
            "H.E.R.E. core functions section must be present",
        )

    def test_here_core_functions_listed(self):
        functions = ["::RECALL", "::GHOSTW4LK", "::ECHO_SPEAK", "::INSERT", "::LOOPBACK"]
        for fn in functions:
            with self.subTest(fn=fn):
                self.assertIn(fn, self.content, f"Core function {fn} must be defined")

    def test_here_design_system_elements(self):
        elements = ["Walls", "Floor", "Air", "Door", "Color scheme"]
        for elem in elements:
            with self.subTest(element=elem):
                self.assertIn(elem, self.content, f"Design element '{elem}' must be defined")


class TestLiminalRooms(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = ROOM_FILE.read_text(encoding="utf-8")

    LIMINAL_ROOMS = [
        ("AA13", "NOWHERE", "_"),
        ("AA14", "SOMEWHERE", "~"),
        ("AA15", "BACKTHEN", "<<"),
        ("AA16", "NEVERW4S", "?!"),
    ]

    def test_all_liminal_room_ids_present(self):
        for room_id, room_name, _ in self.LIMINAL_ROOMS:
            with self.subTest(room=room_name):
                self.assertIn(room_id, self.content, f"Liminal room ID {room_id} must appear")
                self.assertIn(room_name, self.content, f"Liminal room name {room_name} must appear")

    def test_liminal_room_symbols_defined(self):
        """Each liminal room must define its symbolic operator in backtick notation."""
        for room_id, room_name, symbol in self.LIMINAL_ROOMS:
            with self.subTest(room=room_name):
                pattern = rf"AA\d+::{re.escape(room_name)}"
                match = re.search(pattern, self.content)
                self.assertIsNotNone(match, f"Room ID pattern for {room_name} must exist")
                window = self.content[match.start() : match.start() + 700]
                self.assertIn(
                    f"`{symbol}`",
                    window,
                    f"Room {room_name} must define its symbol `{symbol}`",
                )

    def test_liminal_rooms_have_use_cases(self):
        """Each liminal room must document a Use case."""
        for _, room_name, _ in self.LIMINAL_ROOMS:
            with self.subTest(room=room_name):
                pattern = rf"AA\d+::{re.escape(room_name)}"
                match = re.search(pattern, self.content)
                self.assertIsNotNone(match)
                window = self.content[match.start() : match.start() + 700]
                self.assertIn("Use case", window, f"Room {room_name} must document a Use case")


class TestRecursiveFunctions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = ROOM_FILE.read_text(encoding="utf-8")

    def test_warp_to_defined(self):
        self.assertIn("def warp_to", self.content, "warp_to() must be defined")

    def test_echo_from_defined(self):
        self.assertIn("def echo_from", self.content, "echo_from() must be defined")

    def test_flatten_all_defined(self):
        self.assertIn("def flatten_all", self.content, "flatten_all() must be defined")

    def test_room_map_ascii_art_present(self):
        """The visual ASCII room map linking primary rooms must be present."""
        self.assertIn("[E.V.E.R.Y.W.H.E.R.E.]", self.content,
                      "ASCII room-map must be present")


class TestActiveProtocols(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = ROOM_FILE.read_text(encoding="utf-8")

    REQUIRED_PROTOCOLS = [
        "RECURSION_ENGINE",
        "SPATIAL_MEMORY",
        "GHOSTWALK",
        "LIMINAL_ROOM_EXPANSION",
        "STREET_MYTHOS_ENGINE",
    ]

    def test_active_protocols_listed(self):
        for proto in self.REQUIRED_PROTOCOLS:
            with self.subTest(protocol=proto):
                self.assertIn(proto, self.content, f"Protocol {proto} must be listed")


class TestSymbolicStreets(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = ROOM_FILE.read_text(encoding="utf-8")

    def test_emotion_categories_defined(self):
        categories = ["EMOTION::LONGING", "EMOTION::FEAR", "EMOTION::FAME"]
        for cat in categories:
            with self.subTest(category=cat):
                self.assertIn(cat, self.content, f"Emotion category {cat} must be defined")

    def test_archetypal_streets_present(self):
        streets = ["Ocean Avenue", "Mulholland Drive", "Memory Lane", "Broadway", "Route 66"]
        for street in streets:
            with self.subTest(street=street):
                self.assertIn(street, self.content, f"Symbolic street '{street}' must be present")

    def test_room_count_complete(self):
        """All eight room IDs AA09 through AA16 must appear in the document."""
        for i in range(9, 17):
            room_id = f"AA{i:02d}"
            with self.subTest(room_id=room_id):
                self.assertIn(room_id, self.content, f"Room ID {room_id} must be referenced")


if __name__ == "__main__":
    unittest.main(verbosity=2)
