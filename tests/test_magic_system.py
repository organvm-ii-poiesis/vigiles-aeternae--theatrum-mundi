"""
Structural integrity tests for rpg/MAGIC-SYSTEM.md.

The document defines the five core Vigiles magic mechanics and their RPG,
narrative, and system semantics. These tests verify that the mechanics,
interaction model, instability scale, and synth ancestry mappings remain
complete and internally aligned.
"""
import re
import unittest
from pathlib import Path


MAGIC_FILE = Path(__file__).parent.parent / "rpg" / "MAGIC-SYSTEM.md"


class MagicSystemTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.content = MAGIC_FILE.read_text(encoding="utf-8")
        cls.lines = cls.content.splitlines()

    @classmethod
    def section_for(cls, heading):
        pattern = rf"^### \d+\. {re.escape(heading)}\b.*$"
        match = re.search(pattern, cls.content, flags=re.MULTILINE)
        if match is None:
            raise AssertionError(f"Section for {heading} must be present")
        next_match = re.search(r"^### \d+\. ", cls.content[match.end() :], flags=re.MULTILINE)
        end = match.end() + next_match.start() if next_match else len(cls.content)
        return cls.content[match.start() : end]


class TestMagicSystemFileExists(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(MAGIC_FILE.exists(), f"Expected magic system file at {MAGIC_FILE}")

    def test_file_is_not_empty(self):
        self.assertGreater(MAGIC_FILE.stat().st_size, 0, "Magic system file must not be empty")


class TestDocumentStructure(MagicSystemTestCase):
    def test_starts_with_h1_heading(self):
        self.assertTrue(
            self.lines[0].startswith("# "),
            "Document must begin with an H1 heading",
        )

    def test_title_names_all_five_mechanics(self):
        title = self.lines[0].upper()
        for mechanic in ("ABSORB", "FUSE", "EVOLVE", "REPLICATE", "RELINQUISH"):
            with self.subTest(mechanic=mechanic):
                self.assertIn(mechanic, title, f"H1 title must name {mechanic}")

    def test_required_major_sections_present(self):
        sections = [
            "## The Five Mechanics",
            "## Power Interaction Matrix",
            "## Instability Scale",
            "## Connection to Alchemical-Synthesizer Ancestry",
        ]
        for section in sections:
            with self.subTest(section=section):
                self.assertIn(section, self.content, f"Section '{section}' must be present")


class TestCoreMechanics(MagicSystemTestCase):
    MECHANICS = [
        ("ABSORB", "signal_intake(source)"),
        ("FUSE", "binding_matrix(source_a, source_b)"),
        ("EVOLVE", "mutation_constraints(entity, cycle_count)"),
        ("REPLICATE", "clone_bus(source, count)"),
        ("RELINQUISH", "parasitic_absorption(host, target)"),
    ]

    def test_mechanics_declared_in_order_with_function_signatures(self):
        last_index = -1
        for position, (mechanic, signature) in enumerate(self.MECHANICS, start=1):
            heading = f"### {position}. {mechanic}"
            with self.subTest(mechanic=mechanic):
                index = self.content.find(heading)
                self.assertGreater(index, last_index, f"{mechanic} must appear in sequence")
                self.assertIn(f"`{signature}`", self.section_for(mechanic))
                last_index = index

    def test_each_mechanic_has_three_semantic_lenses_and_rules(self):
        lenses = ("**RPG:**", "**Narrative:**", "**System:**", "**Rules:**")
        for mechanic, _ in self.MECHANICS:
            section = self.section_for(mechanic)
            with self.subTest(mechanic=mechanic):
                for lens in lenses:
                    self.assertIn(lens, section, f"{mechanic} must define {lens}")
                rule_count = len(re.findall(r"^- ", section, flags=re.MULTILINE))
                self.assertGreaterEqual(rule_count, 4, f"{mechanic} must include at least four rules")

    def test_mechanic_constraints_preserve_failure_modes(self):
        expected_constraints = {
            "ABSORB": ["corpus access", "RAW", "decay timer"],
            "FUSE": ["Forbidden fusions", "Phaethon Warning", "Witnesses record"],
            "EVOLVE": ["Agon cycle", "irreversible", "Witnesses record"],
            "REPLICATE": ["Smith Containment Protocol", "terminated", "inherits the original's constraints"],
            "RELINQUISH": ["Only one Relinquished bond", "Duration is limited", "Cosmogonist is forbidden"],
        }
        for mechanic, required_phrases in expected_constraints.items():
            section = self.section_for(mechanic)
            for phrase in required_phrases:
                with self.subTest(mechanic=mechanic, phrase=phrase):
                    self.assertIn(phrase, section, f"{mechanic} must preserve constraint '{phrase}'")


class TestPowerInteractionMatrix(MagicSystemTestCase):
    def test_matrix_code_block_present(self):
        matrix_section = self.content.split("## Power Interaction Matrix", 1)[1]
        matrix_section = matrix_section.split("## Instability Scale", 1)[0]
        self.assertIn("```", matrix_section, "Power Interaction Matrix must include a code block")
        for mechanic in ("ABSORB", "FUSE", "EVOLVE", "REPLICATE", "RELINQUISH"):
            with self.subTest(mechanic=mechanic):
                self.assertIn(mechanic, matrix_section, f"Matrix must include {mechanic}")

    def test_interaction_edges_explained(self):
        edges = [
            ("Absorb feeds Fuse", "raw material"),
            ("Fuse produces unstable hybrids", "Evolution"),
            ("Evolution stabilizes", "further Absorption"),
            ("Replication stress-tests", "chain"),
            ("Relinquish provides temporary access", "preview mode"),
        ]
        for start, outcome in edges:
            with self.subTest(edge=start):
                self.assertRegex(
                    self.content,
                    rf"{re.escape(start)}.*{re.escape(outcome)}",
                    f"Interaction edge '{start}' must explain '{outcome}'",
                )


class TestInstabilityScale(MagicSystemTestCase):
    EXPECTED_LEVELS = {
        "0": "Stable",
        "1-3": "Vibrating",
        "4-6": "Volatile",
        "7-9": "Critical",
        "10": "Phaethon",
    }

    def test_instability_table_defines_all_levels(self):
        for level, name in self.EXPECTED_LEVELS.items():
            with self.subTest(level=level):
                pattern = rf"(?m)^\| {re.escape(level)} \| {re.escape(name)} \| .+ \|$"
                self.assertRegex(
                    self.content,
                    pattern,
                    f"Instability level {level} must map to {name}",
                )

    def test_critical_and_phaethon_levels_define_containment_pressure(self):
        phrases = [
            "Must Evolve or abandon",
            "Containment breach",
            "Chronicle records the fall",
        ]
        for phrase in phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, self.content)


class TestSynthAncestry(MagicSystemTestCase):
    EXPECTED_ROWS = {
        "Absorb": ("Signal Intake Ports + Feature Extraction", "Absorption Layer (B1, B2)"),
        "Fuse": ("Fusion Matrix + Composite Voice", "Fusion Layer (C1, C2)"),
        "Evolve": ("Evolution Constraints + Mutation Rate Limiter", "Evolution Layer (C3)"),
        "Replicate": ("Clone Bus + Convergence Decay", "Agent Smith Replication Matrix"),
        "Relinquish": ("Parasitic Absorption + Single-Source Lock", "Relinquished Binding Core"),
    }

    def test_all_mechanics_have_synth_ancestry_rows(self):
        for mechanic, (ancestor, module) in self.EXPECTED_ROWS.items():
            with self.subTest(mechanic=mechanic):
                row_pattern = (
                    rf"(?m)^\| {re.escape(mechanic)} \| {re.escape(ancestor)} "
                    rf"\| {re.escape(module)} \|$"
                )
                self.assertRegex(
                    self.content,
                    row_pattern,
                    f"{mechanic} must map to its synth ancestor and module",
                )

    def test_ancestry_section_states_creatures_are_lab_for_physics(self):
        self.assertIn(
            "The synth creatures were the R&D lab",
            self.content,
            "Ancestry section must preserve the lab-to-world relationship",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
