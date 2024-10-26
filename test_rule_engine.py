from rule_engine import create_rule, combine_rules, evaluate

# Test for create_rule function
def test_create_rule():
    rule = create_rule("age > 18")
    print(f"Created rule condition: {rule.condition}")  # Debugging output
    assert rule.condition == "age > 18", "Rule creation failed for a simple condition."
    print("test_create_rule passed.")

# Test for combine_rules function
def test_combine_rules():
    combined = combine_rules(["age > 18", "income > 30000"])
    print(f"Combined rule condition: {combined.condition}")  # Debugging output
    assert combined.condition == "OR", "Combined rule should have OR as the root."
    assert combined.left.condition == "age > 18", "Left child of combined rule is incorrect."
    assert combined.right.condition == "income > 30000", "Right child of combined rule is incorrect."
    print("test_combine_rules passed.")

# Test for evaluate function
def test_evaluate_rule():
    rule = create_rule("age > 18")
    user_data = {'age': 20}
    assert evaluate(rule, user_data) is True, "Evaluation failed for age > 18."
    
    user_data = {'age': 17}
    assert evaluate(rule, user_data) is False, "Evaluation failed for age <= 18."
    
    print("test_evaluate_rule passed.")

# Run the tests
if __name__ == "__main__":
    test_create_rule()
    test_combine_rules()
    test_evaluate_rule()
