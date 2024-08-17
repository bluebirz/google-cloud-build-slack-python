import json
from src.operators.component_extractors import get_repo
import unittest


class TestMessageExtraction(unittest.TestCase):
    def setUp(self):
        filepath = "tests/sample-payload.json"
        with open(filepath, "r") as fptr:
            self.mock_payload = json.load(fptr)
        print(self.mock_payload)

    def test_get_status(self):
        pass

    def test_get_repo(self):
        pass

    def test_get_branch(self):
        pass

    def test_get_project_id(self):
        pass

    def test_get_duration(self):
        pass

    def test_get_build_url(self):
        pass


# class TestMyFunctions(unittest.TestCase):
#     def test_adder_simple_by_both_positive(self):
#         self.assertEqual(main.adder_simple(1, 1), 2)
#         self.assertEqual(main.adder_simple(2, 2), 4)
#
#     def test_adder_simple_by_both_negative(self):
#         self.assertEqual(main.adder_simple(-1, -1), -2)
#         self.assertEqual(main.adder_simple(-2, -2), -4)
#
#     def test_adder_simple_by_pos_and_neg(self):
#         self.assertEqual(main.adder_simple(-2, 2), 0)
#         self.assertEqual(main.adder_simple(3, -5), -2)
#

if __name__ == "__main__":
    unittest.main()
