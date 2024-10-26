import unittest
from rule_engine import create_rule, combine_rules, evaluate_rule

class TestRuleEngine(unittest.TestCase):
    def test_create_rule(self):
        node = create_rule("age > 18")
        self.assertIsNotNone(node)

    def test_combine_rules(self):
        rules = ["age > 18", "income > 30000"]
        combined = combine_rules(rules)
        self.assertIsNotNone(combined)

    def test_evaluate_rule(self):
        rules = ["age > 18", "income > 30000"]
        combined = combine_rules(rules)
        data = {"age": 20, "income": 35000}
        result = evaluate_rule(combined, data)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
