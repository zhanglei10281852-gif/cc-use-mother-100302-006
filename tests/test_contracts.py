"""具身机器人能力集成门禁基础契约测试。"""

import unittest

from robot_integration import CapabilityRelease, unique_by_identity


class ContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.values = {'release_code': 'release-code-001', 'robot_family': 'robot-family-001', 'capability': 'capability-001', 'state': 'draft'}

    def test_fingerprint_is_stable(self) -> None:
        left = CapabilityRelease(**self.values)
        right = CapabilityRelease(**dict(reversed(list(self.values.items()))))
        self.assertEqual(left.fingerprint(), right.fingerprint())

    def test_evolve_keeps_original(self) -> None:
        original = CapabilityRelease(**self.values)
        change_key = next(key for key, value in self.values.items() if isinstance(value, str))
        changed = original.evolve(**{change_key: "revised-value"})
        self.assertNotEqual(original.fingerprint(), changed.fingerprint())
        self.assertEqual(getattr(original, change_key), self.values[change_key])

    def test_conflicting_identity_is_rejected(self) -> None:
        first = CapabilityRelease(**self.values)
        changed_values = dict(self.values)
        change_key = next(key for key in self.values if key != "release_code")
        changed_values[change_key] = 2 if isinstance(changed_values[change_key], int) else "conflict"
        second = CapabilityRelease(**changed_values)
        with self.assertRaises(ValueError):
            unique_by_identity([first, second])


if __name__ == "__main__":
    unittest.main()
